#!/usr/bin/env python3
"""
Export Markdown (.md) files to Word (.docx) using Pandoc.

Usage:
  python scripts/export_md_to_docx.py <source_dir> <output_dir>
  python scripts/export_md_to_docx.py MD/IAI DOCX/IAI
  python scripts/export_md_to_docx.py MD/Thread DOCX/Thread

Creates one .docx per .md in source_dir, written to output_dir.
Requires Pandoc: https://pandoc.org/installing.html
"""
import argparse
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Export .md files to .docx via Pandoc")
    parser.add_argument("source_dir", type=str, help="Folder containing .md files")
    parser.add_argument("output_dir", type=str, help="Folder to write .docx files")
    args = parser.parse_args()

    src = Path(args.source_dir)
    out = Path(args.output_dir)

    if not src.is_dir():
        print(f"Error: source directory not found: {src}", file=sys.stderr)
        sys.exit(1)

    out.mkdir(parents=True, exist_ok=True)

    md_files = sorted(src.glob("*.md"))
    if not md_files:
        print(f"No .md files in {src}")
        return

    ok = 0
    for md in md_files:
        docx = out / (md.stem + ".docx")
        try:
            subprocess.run(
                ["pandoc", str(md), "-o", str(docx)],
                check=True,
                capture_output=True,
                text=True,
            )
            print(f"  [OK] {md.name} -> {docx.name}")
            ok += 1
        except subprocess.CalledProcessError as e:
            print(f"  [FAIL] {md.name}: {e.stderr or e}", file=sys.stderr)
        except FileNotFoundError:
            print("Error: Pandoc not found. Install from https://pandoc.org/installing.html", file=sys.stderr)
            sys.exit(1)

    print(f"Done. Exported {ok}/{len(md_files)} documents to {out}")


if __name__ == "__main__":
    main()
