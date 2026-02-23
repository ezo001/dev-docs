#!/usr/bin/env python3
"""
Bulk compress images under MD/*/media (and optionally DOCX) to reduce
deployment size for Azure Static Web Apps (500 MB limit).

Requires: pip install Pillow

Usage:
  python compress_media_images.py              # compress MD/AOT, MD/IAI, MD/Thread media
  python compress_media_images.py --dry-run   # report only, no changes
  python compress_media_images.py MD/IAI      # only MD/IAI/media
"""

import argparse
import os
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow is required. Run: pip install Pillow", file=sys.stderr)
    sys.exit(1)

# Formats we compress
IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg"}
# Skip SVGs (already small, and we don't want to rasterize)
# Skip .emf (would need different handling)
MAX_DIMENSION = 1200  # shrink very large images to this on longest side (lower = smaller files)
JPEG_QUALITY = 78     # lower = smaller files, 78–85 is a good range
PNG_OPTIMIZE = True  # PNG: optimize only (no quality param for lossless)


def compress_image(path: Path, dry_run: bool) -> int:
    """Compress one image in place. Returns bytes saved (0 if error or no change)."""
    try:
        img = Image.open(path)
    except Exception as e:
        print(f"  Skip (open failed): {path} - {e}", file=sys.stderr)
        return 0

    if path.suffix.lower() == ".svg":
        return 0

    original_size = path.stat().st_size
    need_resize = (img.width > MAX_DIMENSION or img.height > MAX_DIMENSION) and img.width and img.height
    if need_resize:
        ratio = min(MAX_DIMENSION / img.width, MAX_DIMENSION / img.height)
        new_size = (int(img.width * ratio), int(img.height * ratio))
        img = img.resize(new_size, Image.Resampling.LANCZOS)

    try:
        if path.suffix.lower() in (".jpg", ".jpeg"):
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            if not dry_run:
                img.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        elif path.suffix.lower() == ".png":
            if img.mode == "P" and "transparency" in img.info:
                img = img.convert("RGBA")
            elif img.mode == "P":
                img = img.convert("RGB")
            if not dry_run:
                img.save(path, "PNG", optimize=PNG_OPTIMIZE)
        else:
            return 0
    except Exception as e:
        print(f"  Skip (save failed): {path} - {e}", file=sys.stderr)
        return 0

    if dry_run:
        print(f"  [dry-run] {path.relative_to(path.parents[2])}: {original_size // 1024} KB")
        return 0
    new_size = path.stat().st_size
    saved = max(0, original_size - new_size)
    if saved or need_resize:
        print(f"  {path.relative_to(path.parents[2])}: {original_size // 1024} KB -> {new_size // 1024} KB (saved {saved // 1024} KB)")
    return saved


def main():
    ap = argparse.ArgumentParser(description="Bulk compress images in MD/*/media")
    ap.add_argument("roots", nargs="*", default=["MD/AOT", "MD/IAI", "MD/Thread"],
                    help="Root folders to scan (default: MD/AOT MD/IAI MD/Thread)")
    ap.add_argument("--dry-run", action="store_true", help="Report only, do not modify files")
    args = ap.parse_args()

    base = Path(__file__).resolve().parent
    total_saved = 0
    total_files = 0

    for root in args.roots:
        media_dir = base / root / "media"
        if not media_dir.is_dir():
            print(f"Skipping (no media dir): {media_dir}")
            continue
        print(f"Scanning {media_dir} ...")
        for path in sorted(media_dir.rglob("*")):
            if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS:
                total_saved += compress_image(path, args.dry_run)
                total_files += 1

    print(f"\nTotal files processed: {total_files}")
    print(f"Total bytes saved: {total_saved // 1024} KB ({total_saved // (1024*1024)} MB)")
    if args.dry_run:
        print("(Dry run: no files were modified)")


if __name__ == "__main__":
    main()
