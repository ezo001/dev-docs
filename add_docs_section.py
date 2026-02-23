#!/usr/bin/env python3
"""
Add a new docs section (landing page + config) under MD/.

Creates:
- MD/<folder>/intro.md (landing page with slug: /)
- sidebars-<id>.js
- Updates docusaurus.config.js (plugin path: MD/<folder>, navbar item)

Usage:
  python add_docs_section.py aot "AOT Foundation"
  python add_docs_section.py aot "AOT Foundation" --md-folder AOT   # path = MD/AOT (match DOCX/AOT → MD/AOT)
  python add_docs_section.py my-asset "My Asset"                     # path = MD/my-asset by default

Converted markdown from DOCX/<folder> goes to MD/<folder>; the site reads from there (no copy step).
"""

import argparse
import os
import re
import sys
from pathlib import Path


def id_to_sidebar_name(section_id: str) -> str:
    """e.g. industrial-ai -> industrialAiSidebar, aot -> aotSidebar."""
    parts = section_id.split("-")
    camel = parts[0].lower() + "".join(p.title() for p in parts[1:])
    return f"{camel}Sidebar"


def add_plugin_and_navbar(
    config_path: Path, section_id: str, label: str, md_path: str
) -> None:
    """Append new docs plugin and navbar item to docusaurus.config.js."""
    path_name = md_path  # e.g. MD/AOT
    sidebar_path = f"./sidebars-{section_id}.js"
    sidebar_var = id_to_sidebar_name(section_id)
    route = f"/{section_id}/"

    with open(config_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if already present
    if f"id: '{section_id}'" in content or f'id: "{section_id}"' in content:
        print(f"  Config already has section '{section_id}'; skipping config update.")
        return

    # Insert new plugin: replace "    }],\n  ],\n\n  themeConfig" with plugin + closing bracket
    plugin_insert = (
        "    }],\n"
        f"    ['@docusaurus/plugin-content-docs', {{\n"
        f"      id: '{section_id}',\n"
        f"      path: '{path_name}',\n"
        f"      routeBasePath: '{section_id}',\n"
        f"      sidebarPath: '{sidebar_path}',\n"
        "      editUrl: 'https://github.com/eolson1967/docusaurus-foundations/edit/main/',\n"
        "    }],\n"
        "  ],\n\n"
        "  themeConfig:"
    )
    old_plugins_end = re.compile(
        r"    \}\],\s*\n  \],\s*\n\n  themeConfig:"
    )
    if not old_plugins_end.search(content):
        raise SystemExit("Could not find plugins array end in docusaurus.config.js")
    content = old_plugins_end.sub(plugin_insert, content, count=1)

    # Insert navbar item: add after the last item in themeConfig.navbar.items
    nav_item = f"        {{to: '{route}', label: '{label}', position: 'left'}},\n"
    items_pattern = re.compile(
        r"(items: \[\s*\n)(.*?)(\s*\],\s*\n\s*\},\s*\n\s*prism:)"
    )
    match = items_pattern.search(content, re.DOTALL)
    if not match:
        raise SystemExit("Could not find navbar items in docusaurus.config.js")
    prefix, items, suffix = match.groups()
    new_items = items.rstrip() + "\n" + nav_item
    content = (
        content[: match.start()] + prefix + new_items + suffix + content[match.end() :]
    )

    with open(config_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Updated {config_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Add a new docs section (landing page + Docusaurus config)."
    )
    parser.add_argument(
        "id",
        help="Section ID for URL and paths (e.g. aot -> /aot/, docs-aot, sidebars-aot.js)",
    )
    parser.add_argument(
        "label",
        nargs="?",
        default=None,
        help="Navbar label (default: ID with first letter capitalized)",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Intro page title (default: same as label)",
    )
    parser.add_argument(
        "--config",
        default="docusaurus.config.js",
        help="Path to docusaurus.config.js",
    )
    parser.add_argument(
        "--md-folder",
        default=None,
        help="MD subfolder name (e.g. AOT). Default: same as id. Use to match DOCX/<name> → MD/<name>.",
    )
    args = parser.parse_args()

    section_id = args.id.strip().lower().replace(" ", "-")
    label = args.label or section_id.replace("-", " ").title()
    if args.title:
        intro_title = args.title
    else:
        intro_title = label

    # MD folder: e.g. AOT for path MD/AOT, or aot for path MD/aot
    md_folder = args.md_folder.strip() if args.md_folder else section_id
    md_path = f"MD/{md_folder}"

    root = Path(__file__).resolve().parent
    config_path = root / args.config

    if not config_path.is_file():
        print(f"Error: Config not found: {config_path}")
        sys.exit(1)

    print(f"Adding docs section: id={section_id}, label={label}, path={md_path}")
    print()

    # 1. Create MD/<folder>/intro.md (Accenture-style landing)
    md_dir = root / "MD" / md_folder
    md_dir.mkdir(parents=True, exist_ok=True)
    intro_path = md_dir / "intro.md"
    intro_content = f"""---
id: intro
slug: /
title: {intro_title}
sidebar_position: 1
---

<div className="landing-accenture">

<p className="landing-tagline">Let there be change</p>

<h1 className="landing-headline">{intro_title}</h1>

<p className="landing-sub">Use the sidebar to navigate.</p>

</div>
"""
    intro_path.write_text(intro_content, encoding="utf-8")
    print(f"  Created {intro_path}")

    # 2. Create sidebars-<id>.js
    sidebar_var = id_to_sidebar_name(section_id)
    sidebars_path = root / f"sidebars-{section_id}.js"
    sidebars_content = f"""module.exports = {{
  {sidebar_var}: [{{type: 'autogenerated', dirName: '.'}}],
}};
"""
    sidebars_path.write_text(sidebars_content, encoding="utf-8")
    print(f"  Created {sidebars_path}")

    # 3. Update docusaurus.config.js (plugin path = MD/<folder>)
    add_plugin_and_navbar(config_path, section_id, label, md_path)

    print()
    print("Done. Next steps:")
    print(f"  1. Put .docx in DOCX/{md_folder}/ and run: python convert_docx_to_markdown.py --all")
    print(f"  2. Run: npm start")
    print(f"  3. Open: http://localhost:3000/{section_id}/")


if __name__ == "__main__":
    main()
