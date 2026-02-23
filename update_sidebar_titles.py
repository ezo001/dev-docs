#!/usr/bin/env python3
"""
Update frontmatter 'title' in all markdown files under a directory so that
sidebar labels match the current filename (e.g. after renaming to remove version IDs).

Usage:
  python update_sidebar_titles.py              # default: MD/
  python update_sidebar_titles.py MD/Thread    # only one asset folder
  python update_sidebar_titles.py --dry-run   # print changes without writing
"""

import argparse
import os
import re
from pathlib import Path


def filename_to_title(filename: str) -> str:
    """Convert a filename (no path, no .md) to a readable sidebar title."""
    # Remove .md
    name = filename.replace(".md", "").strip()
    # Replace underscores with spaces
    title = name.replace("_", " ")
    # Strip trailing/leading spaces and underscores
    title = title.strip().strip("_").strip()
    # Collapse multiple spaces
    title = " ".join(title.split())
    return title


def update_frontmatter_title(content: str, new_title: str) -> str:
    """Replace the first 'title: ...' line in the frontmatter (between first --- and second ---)."""
    if "---" not in content:
        return content
    parts = content.split("---", 2)
    if len(parts) < 3:
        return content
    before, frontmatter, after = parts[0], parts[1], parts[2]
    # Replace title line (allow optional space after colon)
    new_line = f"title: {new_title}"
    frontmatter_new = re.sub(
        r"^title:\s*.+$",
        new_line,
        frontmatter,
        count=1,
        flags=re.MULTILINE,
    )
    if frontmatter_new == frontmatter:
        # No title line found; insert after first line or at start
        lines = frontmatter.strip().split("\n")
        inserted = False
        for i, line in enumerate(lines):
            if line.strip().startswith("sidebar_position"):
                lines.insert(i + 1, new_line)
                inserted = True
                break
        if not inserted:
            lines.insert(0, new_line)
        frontmatter_new = "\n".join(lines) + "\n"
    return before + "---" + frontmatter_new + "---" + after


def main():
    parser = argparse.ArgumentParser(
        description="Update markdown frontmatter titles from filenames (for sidebar labels)."
    )
    parser.add_argument(
        "dir",
        nargs="?",
        default="MD",
        help="Directory to scan (default: MD)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print what would be changed",
    )
    args = parser.parse_args()
    root = Path(args.dir)
    if not root.is_dir():
        print(f"Error: not a directory: {root}")
        return 1
    updated = 0
    skipped = 0
    for path in sorted(root.rglob("*.md")):
        if path.name.startswith("."):
            continue
        # Keep custom titles for intro/landing pages
        if path.name.lower() == "intro.md":
            skipped += 1
            continue
        new_title = filename_to_title(path.name)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        old_match = re.search(r"^title:\s*(.+)$", content, re.MULTILINE)
        old_title = old_match.group(1).strip() if old_match else "(none)"
        if old_title == new_title:
            skipped += 1
            continue
        new_content = update_frontmatter_title(content, new_title)
        if new_content == content:
            skipped += 1
            continue
        print(f"  {path.relative_to(root)}")
        print(f"    title: {old_title!r} -> {new_title!r}")
        if not args.dry_run:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
        updated += 1
    print(f"\nUpdated: {updated} file(s)" + (" (dry run)" if args.dry_run else ""))
    if skipped:
        print(f"Skipped (unchanged): {skipped} file(s)")
    return 0


if __name__ == "__main__":
    exit(main())
