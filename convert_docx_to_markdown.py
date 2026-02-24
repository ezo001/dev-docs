#!/usr/bin/env python3
"""
Unified Word (.docx) to Markdown converter for Docusaurus/MDX.

Converts all .docx in a directory to .md with:
- Pandoc conversion with image extraction (--extract-media)
- Grid tables → pipe tables
- HTML tag removal
- Curly brace escaping (MDX-safe, preserves code blocks)
- Ampersand and angle-bracket fixes for MDX
- Image path fixing (docs/media/ → media/)
- Docusaurus frontmatter (sidebar_position, title)

Usage:
  python convert_docx_to_markdown.py                    # prompts for source and output paths
  python convert_docx_to_markdown.py word_docs docs     # word_docs → docs/ (no prompt)
  python convert_docx_to_markdown.py . docs --no-clear  # keep existing .md files
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path


def parse_grid_table(table_lines):
    """Parse grid table and convert to pipe table with all cells on one line."""
    data_rows = []
    current_row_cells = []

    for line in table_lines:
        stripped = line.strip()
        if not stripped.startswith("|") or all(c in "|+- =" for c in stripped):
            continue
        cells = stripped.split("|")[1:-1]
        if stripped.startswith("|"):
            if current_row_cells:
                data_rows.append(current_row_cells)
                current_row_cells = []
            current_row_cells = [cell.strip() for cell in cells]
        else:
            for i, cell in enumerate(cells):
                if i < len(current_row_cells):
                    current_row_cells[i] += " " + cell.strip()
    if current_row_cells:
        data_rows.append(current_row_cells)

    if not data_rows:
        return []

    pipe_rows = []
    for cells in data_rows:
        cleaned_cells = []
        for cell in cells:
            cell = re.sub(r"<[^>]+>", "", cell)
            cell = " ".join(cell.split())
            cleaned_cells.append(cell)
        if any(cleaned_cells):
            pipe_rows.append("| " + " | ".join(cleaned_cells) + " |")

    if len(pipe_rows) > 1:
        num_cols = pipe_rows[0].count("|") - 1
        separator = "| " + " | ".join(["---"] * num_cols) + " |"
        pipe_rows.insert(1, separator)
    return pipe_rows


def convert_grid_tables_to_pipe(content):
    """Convert all grid tables to pipe tables (plus-style and dash-style)."""
    content = _convert_plus_grid_tables(content)
    content = _convert_dash_grid_tables(content)
    return content


def _convert_plus_grid_tables(content):
    """Convert plus-style grid tables (lines starting with + or |)."""
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^\s*\+[-=]+\+", line):
            table_lines = []
            while i < len(lines) and (
                lines[i].strip().startswith("+") or lines[i].strip().startswith("|")
            ):
                table_lines.append(lines[i])
                i += 1
            pipe_table = parse_grid_table(table_lines)
            if pipe_table:
                result.append("")
                result.extend(pipe_table)
                result.append("")
            continue
        result.append(line)
        i += 1
    return "\n".join(result)


def _convert_dash_grid_tables(content):
    """Convert dash-style grid tables (  ---  ---  and   col1   col2  ) to pipe tables."""
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Start of dash grid: line of only spaces and dashes/equals
        if re.match(r"^[\s\-=]+$", stripped) and len(stripped) >= 4 and "-" in stripped:
            i += 1
            rows = []  # list of [cell1, cell2]
            while i < len(lines):
                ln = lines[i]
                st = ln.strip()
                # Separator or blank (skip, don't add to rows)
                if re.match(r"^[\s\-=]*$", st) and (not st or "-" in st):
                    i += 1
                    continue
                # Content row: split on 2+ spaces into two parts
                parts = re.split(r"\s{2,}", st, maxsplit=1)
                if len(parts) == 2 and (parts[0] or parts[1]):
                    c1 = " ".join(parts[0].split())
                    c2 = " ".join(parts[1].split())
                    c1 = re.sub(r"<[^>]+>", "", c1)
                    c2 = re.sub(r"<[^>]+>", "", c2)
                    rows.append([c1, c2])
                    i += 1
                    continue
                # Continuation: not a heading, append to last row's second cell
                if rows and st and not st.startswith("#") and not re.match(r"^[\s\-=]+$", st):
                    rows[-1][1] = (rows[-1][1] + " " + st).strip()
                    i += 1
                    continue
                break
            if len(rows) >= 2:
                out = []
                out.append("| " + " | ".join(rows[0]) + " |")
                out.append("| --- | --- |")
                for r in rows[1:]:
                    out.append("| " + " | ".join(r) + " |")
                result.append("")
                result.extend(out)
                result.append("")
                continue
        result.append(line)
        i += 1
    return "\n".join(result)


def escape_curly_braces_safe(content):
    """Escape curly braces except in code blocks and inline code."""
    lines = content.split("\n")
    result = []
    in_code_block = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            result.append(line)
            continue
        if not in_code_block:
            parts = line.split("`")
            for i in range(len(parts)):
                if i % 2 == 0:
                    parts[i] = parts[i].replace("{", "\\{").replace("}", "\\}")
            line = "`".join(parts)
        result.append(line)
    return "\n".join(result)


def fix_ampersands(content):
    """Replace & with &amp; except when already part of an HTML entity."""
    return re.sub(
        r"&(?!(?:lt|gt|amp|nbsp|quot|apos|#\d+|#x[0-9a-fA-F]+);)", "&amp;", content
    )


def fix_angle_brackets(content):
    """Escape standalone angle brackets that MDX might interpret as JSX.
    Preserve leading > on a line (markdown blockquote) so blockquotes and images inside them render.
    """
    lines = content.split("\n")
    fixed = []
    in_code_block = False
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            fixed.append(line)
            continue
        if in_code_block:
            fixed.append(line)
            continue
        # Preserve blockquote: line starting with optional whitespace and > keeps that > so markdown parses it
        m_quote = re.match(r"^(\s*)>(.*)$", line)
        if m_quote:
            prefix = m_quote.group(1) + ">"
            rest = m_quote.group(2)
            rest = re.sub(r"<(?![a-zA-Z/!])", "&lt;", rest)
            rest = re.sub(r"(?<![a-zA-Z/\-])>(?!\s*\n)", "&gt;", rest)
            fixed.append(prefix + rest)
            continue
        line = re.sub(r"<(?![a-zA-Z/!])", "&lt;", line)
        line = re.sub(r"(?<![a-zA-Z/\-])>(?!\s*\n)", "&gt;", line)
        fixed.append(line)
    return "\n".join(fixed)


def preserve_mailto_links(content):
    """Convert mailto HTML links to markdown so the email is retained when we strip HTML."""
    # <a href="mailto:user@example.com">text</a> — Word/Pandoc may add extra attributes or newlines
    def repl(m):
        href = m.group(1).strip()
        inner = (m.group(2) or "").strip()
        # If link text is empty or generic, use the email as the visible text
        if not inner or inner.lower() in ("link", "email", "click here", "here", "mail"):
            inner = href.replace("mailto:", "").strip()
        return f"[{inner}]({href})"

    # Allow optional whitespace/newlines and other attributes between > and </a>
    content = re.sub(
        r'<a\s+href\s*=\s*["\'](mailto:[^"\']+)["\'][^>]*>\s*(.*?)\s*</a>',
        repl,
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return content


def preserve_hyperlink_links(content):
    """Convert remaining HTML <a href="..."> links (e.g. video URLs, web links) to markdown
    so they are retained when we strip HTML. Run after preserve_mailto_links.
    When the link wraps an image (e.g. video thumbnail with right-click Link > Address),
    output markdown linked-image syntax so both the image and the video URL are preserved.
    Video links in these docs typically use https://greetings.accenture.com (normalized later).
    """
    # Match <img ...> and extract src= and alt= (attributes can be in any order)
    def extract_img_src_alt(html):
        src_m = re.search(r'src\s*=\s*["\']([^"\']+)["\']', html, re.IGNORECASE)
        alt_m = re.search(r'alt\s*=\s*["\']([^"\']*)["\']', html, re.IGNORECASE)
        if src_m:
            return src_m.group(1).strip(), (alt_m.group(1).strip() if alt_m else "")
        return None

    def repl(m):
        href = (m.group(1) or "").strip()
        inner = (m.group(2) or "").strip()
        if not href:
            return m.group(0)
        # Linked image (e.g. video thumbnail): <a href="video-url"><img src="..." alt="..."></a>
        if "<img" in inner.lower():
            img_info = extract_img_src_alt(inner)
            if img_info:
                img_src, img_alt = img_info
                # Normalize image path: Pandoc may emit docs/media/ or full path; we use media/ for Docusaurus
                if "docs/media/" in img_src:
                    img_src = img_src.replace("docs/media/", "media/")
                return f"[![{img_alt}]({img_src})]({href})"
        # Text link
        if not inner or inner.lower() in ("link", "click here", "here", "video", "watch"):
            inner = href
        inner = inner.replace("[", "\\[").replace("]", "\\]")
        return f"[{inner}]({href})"

    # Match <a href="url">...</a> (any URL except mailto, already handled). Allow extra attributes.
    content = re.sub(
        r'<a\s+href\s*=\s*["\']([^"\']+)["\'][^>]*>\s*(.*?)\s*</a>',
        repl,
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    return content


def normalize_greetings_video_urls(content):
    """Fix video URLs: all video links use https://greetings.accenture.com; normalize any
    accidental space in the domain (e.g. greetings. accenture.com -> greetings.accenture.com).
    """
    # Fix space in domain inside markdown link targets: ](https://greetings. accenture.com -> ](https://greetings.accenture.com
    content = re.sub(
        r"(\]\(https?://)greetings\.\s*accenture\.com",
        r"\1greetings.accenture.com",
        content,
        flags=re.IGNORECASE,
    )
    return content


def linkify_raw_urls(content):
    """Convert raw http(s) URLs in text to markdown links so they are clickable.
    Skips URLs already inside markdown link syntax (](url) or "(url)). Runs after
    HTML strip so any URLs left as plain text by Pandoc get linkified.
    """
    # Only match URL at start of line or after whitespace to avoid touching ](https://...)
    return re.sub(
        r"(^|\s)(https?://[^\s)\)\]\<]+)",
        r"\1[\2](\2)",
        content,
        flags=re.MULTILINE,
    )


def fix_malformed_markdown_links(content):
    r"""Fix markdown links where the URL contains a duplicate/stray ](url) so MDX can parse them.
    E.g. [text](https://aot.accenturedigitalplant.com](https://aot.accenturedigitalplant.com)) or
    [url](https://example.com\) -> collapse to a single valid link.
    Also fix [url](url) (identical link text and URL) which some parsers treat as URL ending at last ).
    """
    # Remove duplicate ](https://... ) or ](http://... ) inside another link's URL (leaves first URL)
    content = re.sub(
        r"(\]\(https?://[^)]*?)(\]\(https?://[^)]+\))+\)",
        r"\1)",
        content,
    )
    # Fix URLs that end with \\) (escaped closing paren) -> remove trailing backslash so URL is valid
    content = re.sub(
        r"(\]\(https?://[^)]*)\\\s*\)",
        r"\1)",
        content,
    )
    # Fix [url](url) where link text and URL are the same http(s) URL - MDX can parse URL as
    # spanning to the last ), producing invalid "url](url". Use short link text so only one ) in link.
    content = re.sub(
        r"\[(https?://[^\]]+)\]\(\1\)",
        r"[link](\1)",
        content,
    )
    # Fix [url\](url) (link text has trailing backslash, same URL) - same MDX parse issue
    content = re.sub(
        r"\[(https?://[^\]]+)\\\]\(\1\)",
        r"[link](\1)",
        content,
    )
    return content


def restore_blockquote_angle(content):
    """Restore > at line start where it was escaped as &gt; so blockquotes (and images in them) render."""
    lines = content.split("\n")
    out = []
    for line in lines:
        # Line that starts with optional whitespace then &gt; (blockquote that was over-escaped)
        if re.match(r"^\s*&gt;", line):
            line = re.sub(r"^(\s*)&gt;", r"\1>", line, count=1)
        out.append(line)
    return "\n".join(out)


def remove_pandoc_underline_attributes(content):
    """Remove Pandoc span attributes (e.g. \\{.underline\\}) so they don't show as literal text.
    [[text]\\{.underline\\}](url) -> [text](url); also strip ]{.underline} and bare \\{.underline\\}.
    """
    # [[text]\{.underline\}](url) -> [text](url)
    content = re.sub(r"\[\[([^\]\[]+)\]\{\\.underline\\\}\]\(", r"[\1](", content)
    # Remove remaining \{.underline\} and ]{.underline}
    content = re.sub(r"\\\{\.underline\\\}", "", content)
    content = re.sub(r"\]\{\.underline\}", "]", content)
    return content


def linkify_video_placeholder_images(content, image_links=None, link_below_image=True):
    """When an image is preceded by text like 'Click on the image to launch a video', add the
    video URL. image_links: optional dict[int, str] from extract_image_hyperlink_urls(docx).
    If link_below_image is True (default), keep the image as a plain image and add a
    '[Watch video](url)' link on the line beneath it. If False, wrap the image in the link.
    """
    image_links = image_links or {}
    lines = content.split("\n")
    result = []
    i = 0
    # Image line: plain ![alt](path) or already linked [![alt](path)](url)
    plain_image = re.compile(r"^(\s*)!\[([^\]]*)\]\((media/[^)]+)\)\s*$")
    already_linked = re.compile(r"^\s*\[\!\[.*\]\(.*\)\]\(https?://")
    # Match media/imageN or media/<doc_stem>/imageN (per-doc media folders)
    image_num_from_path = re.compile(r"media/(?:[^/]+/)?image(\d+)[.\w]*$", re.IGNORECASE)

    while i < len(lines):
        line = lines[i]
        block = " ".join(lines[i : min(i + 10, len(lines))]).lower()
        did_link_below = False
        found_video_image = False
        if (
            ("click" in block and "video" in block)
            or ("launch a video" in block)
            or ("play a video" in block)
            or ("image below" in block and "video" in block)
            or ("video" in block and "depicting" in block)
        ):
            j = i
            while j < min(i + 10, len(lines)):
                stripped = lines[j].strip()
                if already_linked.match(lines[j]):
                    j += 1
                    continue
                m = plain_image.match(lines[j])
                if m:
                    indent, alt, path = m.group(1), m.group(2), m.group(3)
                    num_m = image_num_from_path.search(path)
                    image_num = int(num_m.group(1)) if num_m else None
                    video_url = image_links.get(image_num) if image_num else None
                    if not video_url:
                        video_url = "https://greetings.accenture.com/watch/"
                    if link_below_image:
                        result.append(line)
                        for k in range(i + 1, j):
                            result.append(lines[k])
                        result.append(lines[j])
                        result.append(f"{indent}[Watch video]({video_url})")
                        i = j + 1
                        if i < len(lines) and lines[i].strip() == "":
                            i += 1
                        did_link_below = True
                    else:
                        lines[j] = f"{indent}[![{alt}]({path})]({video_url})"
                        found_video_image = True
                    break
                if stripped and not stripped.startswith("|") and not re.match(r"^[-*]\s", stripped):
                    if re.match(r"^#+\s", stripped):
                        break
                j += 1
            else:
                result.append(line)
            if did_link_below:
                continue  # i already advanced in the link_below block
            if not found_video_image:
                i += 1
                continue  # already appended line in the while's else
        result.append(line)
        i += 1

    return "\n".join(result)


def merge_pipe_table_continuation_rows(content):
    """Merge pipe-table lines that are continuations of the previous row (e.g. first cell empty)
    so that line breaks inside a cell do not split the row. Output keeps each logical row on one line.
    """
    lines = content.split("\n")
    result = []
    i = 0
    table_sep = re.compile(r"^\s*\|[\s\-:|]+\|\s*$")  # | --- | --- |

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Detect pipe table row (starts and ends with |)
        if stripped.startswith("|") and stripped.endswith("|") and not table_sep.match(stripped):
            cells = [c.strip() for c in stripped.split("|")[1:-1]]
            num_cols = len(cells)
            # Look ahead: merge following lines that look like continuation (same col count, first cell empty)
            j = i + 1
            while j < len(lines):
                next_stripped = lines[j].strip()
                if not next_stripped.startswith("|") or not next_stripped.endswith("|"):
                    break
                if table_sep.match(next_stripped):
                    break
                next_cells = [c.strip() for c in next_stripped.split("|")[1:-1]]
                if len(next_cells) != num_cols:
                    break
                # First cell empty (or all but last empty) => continuation of previous row
                first_has_content = bool(next_cells[0]) if next_cells else False
                if not first_has_content and num_cols > 0:
                    # Append continuation to last cell of current row (as one line, use space)
                    last_cell_continuation = " ".join(next_cells[-1].split()) if next_cells else ""
                    if last_cell_continuation:
                        cells[-1] = (cells[-1] + " " + last_cell_continuation).strip()
                    j += 1
                    continue
                break
            # Emit single row
            result.append("| " + " | ".join(cells) + " |")
            i = j
            continue
        result.append(line)
        i += 1

    return "\n".join(result)


def merge_list_continuation_lines(content):
    """Merge bulleted/numbered list lines that are actually continuations of the previous item
    (e.g. Word line break inside one list item). When the next line is a bullet with same level
    and the previous line was a list item, append the new line's text to the previous item so
    the content stays in one list item.
    """
    lines = content.split("\n")
    result = []
    i = 0
    list_item = re.compile(r"^(\s*)([-*]|\d+\.)\s+(.*)$")

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        m = list_item.match(line)
        if m and result:
            prev_m = list_item.match(result[-1])
            if prev_m:
                prev_indent, prev_bullet, prev_text = prev_m.group(1), prev_m.group(2), prev_m.group(3)
                curr_indent, curr_bullet, curr_text = m.group(1), m.group(2), m.group(3)
                # Same bullet style and same or deeper indent: treat as continuation
                same_style = (prev_bullet == curr_bullet or (prev_bullet in "*-" and curr_bullet in "*-"))
                prev_ends_sentence = prev_text.rstrip().endswith(".") or prev_text.rstrip().endswith(":")
                curr_starts_sentence = bool(curr_text) and curr_text[0].isupper()
                # Only merge if this looks like a continuation (prev didn't end sentence, or curr starts lowercase)
                is_continuation = not prev_ends_sentence or (curr_text and not curr_text[0].isupper())
                if same_style and len(curr_indent) >= len(prev_indent) and is_continuation:
                    result[-1] = result[-1].rstrip() + " " + curr_text
                    i += 1
                    continue
        result.append(line)
        i += 1

    return "\n".join(result)


def convert_angle_bracket_emails(content):
    """Convert <email@domain.com> to [email](mailto:...) before HTML strip.
    Pandoc/Word often emit contacts as angle-bracket-wrapped emails; our strip of <[^>]+> would remove them.
    """
    return re.sub(
        r"<([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})>",
        r"[\1](mailto:\1)",
        content,
    )


def linkify_plain_emails(content):
    """Wrap plain email addresses in markdown mailto links so they are preserved and clickable."""
    # Match email not already part of ](mailto:... to avoid double-wrapping
    email_pattern = re.compile(
        r"(?<!mailto:)(?<![(\[])\b([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\b(?![\])])"
    )
    return email_pattern.sub(r"[\1](mailto:\1)", content)


def remove_table_of_contents(content):
    """Remove Word-generated 'Table of Contents' section (heading + following link list)."""
    lines = content.split("\n")
    result = []
    skipping = False
    # Match: Contents / Table of Contents / TOC with optional # or **, and optional Pandoc attributes (e.g. \{#contents .TOC-Heading\})
    toc_heading = re.compile(
        r"^\s*(?:#+\s+)?(?:\*\*)?(?:Table\s+of\s+Contents|Contents|TOC)(?:\*\*)?\s*.*$",
        re.IGNORECASE,
    )
    # TOC entries look like [Some Title [3](#anchor)](#anchor) or [Title](#anchor)
    toc_entry = re.compile(r"^\s*\[.+\]\(#[-a-zA-Z0-9_]+\)\s*$")

    for line in lines:
        stripped = line.strip()
        if toc_heading.match(stripped):
            skipping = True
            result.append("")
            continue
        if skipping:
            # Stop at next ATX heading (# with a word) — start of real content
            if re.match(r"^\s*#+\s+[A-Za-z]", stripped):
                skipping = False
                result.append(line)
                continue
            # Skip lines that look like TOC links
            if toc_entry.match(stripped):
                continue
            continue
        result.append(line)

    return "\n".join(result)


def wrap_metadata_for_agents(content):
    """Wrap the 'Metadata Table' block in a hidden div for AI use only (invisible to humans).
    Also wraps a table starting with | **Field** | **Value** | when there is no 'Metadata Table' heading.
    """
    lines = content.split("\n")
    result = []
    i = 0
    metadata_heading = re.compile(
        r"^\s*(\*\*)?Metadata\s+Table(\*\*)?\s*$", re.IGNORECASE
    )
    metadata_table_first_row = re.compile(
        r"^\s*\|\s*\*\*Field\*\*\s*\|\s*\*\*Value\*\*\s*\|"
    )
    heading_line = re.compile(r"^\s*#+\s+\S")

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if metadata_heading.match(stripped):
            # Start of metadata block: collect until next # heading
            result.append(
                '<div class="metadata-for-agents" aria-hidden="true">'
            )
            result.append(line)
            i += 1
            while i < len(lines) and not heading_line.match(lines[i].strip()):
                result.append(lines[i])
                i += 1
            result.append("</div>")
            result.append("")
            continue
        # No "Metadata Table" heading: wrap table that starts with | **Field** | **Value** |
        if metadata_table_first_row.match(stripped):
            result.append(
                '<div class="metadata-for-agents" aria-hidden="true">'
            )
            result.append(line)
            i += 1
            while i < len(lines) and not heading_line.match(lines[i].strip()):
                result.append(lines[i])
                i += 1
            result.append("</div>")
            result.append("")
            continue
        result.append(line)
        i += 1

    return "\n".join(result)


def format_doc_title_block(content):
    """Replace the top 3–4 line title block (Asset name, topic, doc type, optional Release Version)
    with a styled div so CSS can set 18pt / 24pt / 18pt. Runs after HTML strip so the div is kept.
    """
    lines = content.split("\n")
    # Find body start (after frontmatter --- ... ---)
    body_start_idx = 0
    if content.strip().startswith("---"):
        for idx in range(len(lines)):
            if lines[idx].strip() == "---" and idx > 0:
                body_start_idx = idx + 1
                break
        while body_start_idx < len(lines) and not lines[body_start_idx].strip():
            body_start_idx += 1
    # Collect up to 4 title-block lines (stop at Metadata Table, table row, or # heading)
    title_block_indices = []
    i = body_start_idx
    while i < len(lines) and len(title_block_indices) < 4:
        st = lines[i].strip()
        if not st:
            i += 1
            continue
        if re.match(r"^\s*(\*\*)?Metadata\s+Table(\*\*)?\s*$", st, re.IGNORECASE):
            break
        if st.startswith("|") and "|" in st:
            break
        if re.match(r"^#+\s+\S", st):
            break
        if re.match(r"^<div\s", st):
            break
        title_block_indices.append(i)
        i += 1

    if len(title_block_indices) < 3:
        return content

    def strip_bold(s):
        s = s.strip()
        if s.startswith("**") and s.endswith("**"):
            return s[2:-2].strip()
        return s

    L1 = lines[title_block_indices[0]].strip()
    L2 = lines[title_block_indices[1]].strip()
    L3 = lines[title_block_indices[2]].strip()
    t1, t2, t3 = strip_bold(L1), strip_bold(L2), strip_bold(L3)
    version_line = None
    if len(title_block_indices) > 3:
        L4 = lines[title_block_indices[3]].strip()
        if L4.lower().startswith("release version"):
            version_line = L4
    end_idx = title_block_indices[2] if not version_line else title_block_indices[3]
    # Escape HTML in text so MDX/safe HTML doesn't break
    def esc(s):
        return (
            s.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
        )

    replacement = (
        '<div class="doc-title-block">\n'
        f'<p class="doc-asset-name">{esc(t1)}</p>\n'
        f'<p class="doc-topic">{esc(t2)}</p>\n'
        f'<p class="doc-type">{esc(t3)}</p>\n'
        "</div>\n\n"
    )
    if version_line:
        replacement += f'<p class="doc-version">{esc(version_line)}</p>\n\n'
    new_lines = lines[: title_block_indices[0]] + [replacement.rstrip()] + lines[end_idx + 1 :]
    return "\n".join(new_lines)


def demote_body_headings(content):
    """Demote all ATX headings by one level (# -> ##, ## -> ###, ...) so the first
    content heading (e.g. Introduction) is not H1 and matches desired smaller size.
    """
    def add_one_hash(m):
        return "#" + m.group(0)

    return re.sub(r"^(#{1,6})\s+(.*)$", add_one_hash, content, flags=re.MULTILINE)


def fix_metadata_div_line_breaks(content):
    """Ensure <div and </div> for metadata are on their own lines so MDX parses them (no same-line markdown)."""
    # )</div> or ) </div> on same line -> ) newline </div>
    content = re.sub(r"(\))\s*</div>", r"\1\n</div>", content)
    # )<div on same line -> ) newline <div
    content = re.sub(r"(\))\s*<div", r"\1\n<div", content)
    return content


def replace_emf_with_placeholder(content):
    """Replace .emf image refs with /img/placeholder.png so Docusaurus build doesn't fail (unsupported format)."""
    return re.sub(r"\]\(([^)]+\.emf)\)", r"](/img/placeholder.png)", content, flags=re.IGNORECASE)


def ensure_contacts_section_emails(content):
    """In any '## Contacts' (or '## Contact') section, linkify plain emails and ensure
    standalone email/link lines become list items so contacts are visible after conversion.
    """
    lines = content.split("\n")
    result = []
    i = 0
    contacts_heading = re.compile(r"^\s*#+\s+Contacts?\s*$", re.IGNORECASE)
    atx_heading = re.compile(r"^\s*#+\s+\S")
    email_or_mailto_line = re.compile(
        r"^\s*(\[.*?\]\(mailto:[^)]+\)|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\s*$"
    )
    while i < len(lines):
        line = lines[i]
        if contacts_heading.match(line.strip()):
            result.append(line)
            i += 1
            # Collect block until next ATX heading
            block = []
            while i < len(lines) and not atx_heading.match(lines[i].strip()):
                block.append(lines[i])
                i += 1
            # Linkify plain emails in this block only
            block_text = "\n".join(block)
            block_text = linkify_plain_emails(block_text)
            block_lines = block_text.split("\n")
            for bl in block_lines:
                st = bl.strip()
                # Turn standalone email or mailto link into a list item so it displays
                if st and email_or_mailto_line.match(st) and not re.match(r"^\s*[-*]\s", bl):
                    result.append("-   " + st)
                else:
                    result.append(bl)
            continue
        result.append(line)
        i += 1
    return "\n".join(result)


def clean_markdown_content(content, verbose=True, image_links=None):
    """Full cleanup for Docusaurus/MDX. image_links: optional dict (unused; kept for API compatibility)."""
    if verbose:
        print("  Preserving email (mailto) links...")
    content = preserve_mailto_links(content)
    if verbose:
        print("  Preserving hyperlinks (e.g. video URLs)...")
    content = preserve_hyperlink_links(content)
    if verbose:
        print("  Converting angle-bracket-wrapped emails (<email@x.com>)...")
    content = convert_angle_bracket_emails(content)
    if verbose:
        print("  Wrapping plain email addresses in mailto links...")
    content = linkify_plain_emails(content)
    if verbose:
        print("  Removing table of contents...")
    content = remove_table_of_contents(content)
    if verbose:
        print("  Converting grid tables...")
    content = convert_grid_tables_to_pipe(content)
    if verbose:
        print("  Removing HTML tags...")
    content = re.sub(r"<[^>]+>", "", content)
    # Re-linkify plain emails that were inside stripped tags (e.g. mailto links Pandoc emitted as HTML)
    if verbose:
        print("  Re-wrapping plain emails after HTML strip...")
    content = linkify_plain_emails(content)
    if verbose:
        print("  Linkifying raw URLs...")
    content = linkify_raw_urls(content)
    if verbose:
        print("  Fixing malformed markdown links...")
    content = fix_malformed_markdown_links(content)
    if verbose:
        print("  Escaping curly braces...")
    content = escape_curly_braces_safe(content)
    if verbose:
        print("  Fixing ampersands and angle brackets...")
    content = fix_ampersands(content)
    content = fix_angle_brackets(content)
    if verbose:
        print("  Fixing image paths...")
    content = re.sub(r"!\[([^\]]*)\]\(docs/media/", r"![\1](media/", content)
    # MD/Asset/_pandoc_extract/DocName/media/... -> media/DocName/... (Pandoc extract paths; use forward slashes)
    for asset in ("Thread", "IAI", "AOT", "A4E", "A4M"):
        content = re.sub(
            r"!\[([^\]]*)\]\(MD[/\\]" + asset + r"[/\\]_pandoc_extract[/\\]([^/\\]+)[/\\]media[/\\]([^)]+)\)",
            lambda m: f"![{m.group(1)}](media/{m.group(2)}/{m.group(3).replace(chr(92), '/')})",
            content,
        )
    # Pandoc may write paths like MD/Thread/media/ or MD\Thread\media\ - use media/ for Docusaurus
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]Thread[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]IAI[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]AOT[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]A4E[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]A4M[/\\]media/", r"![\1](media/", content)
    # Docusaurus resolves asset paths relative to the document only when they start with ./
    content = re.sub(r"\]\((media/[^)]+)\)", r"](./\1)", content)
    # Spaces in image URLs break Markdown parsing (URL ends at space); encode as %20
    content = re.sub(
        r"\]\((\./media/[^)]+)\)",
        lambda m: "](" + m.group(1).replace(" ", "%20") + ")",
        content,
    )
    # Normalize image extensions to lowercase so webpack does not see "image26.PNG" vs "image26.png" as different modules
    content = re.sub(
        r"(\]\([^)]*media/[^)]+\.)(PNG|JPG|JPEG|GIF)(\))",
        lambda m: m.group(1) + m.group(2).lower() + m.group(3),
        content,
    )
    # Normalize video URLs (https://greetings.accenture.com); fix accidental space in domain
    content = normalize_greetings_video_urls(content)
    # Wrap video placeholder images (click to launch/play video) in link; use real URL from DOCX when available
    if verbose:
        print("  Linkifying video placeholder images...")
    content = linkify_video_placeholder_images(content, image_links=image_links)
    # Remove Pandoc image attributes \{width="..." height="..."\} so images render (closing can be "} or "\}); keep newline
    content = re.sub(r"\\?\{width=\"[^\"]*\" height=\"[^\"]*\"\}\s*", "\n", content)
    content = re.sub(r"\\?\{width=\"[^\"]*\" height=\"[^\"]*\"\\\}\s*", "\n", content)
    content = re.sub(r"\[<u>([^<]+)</u>\]", r"[\1]", content)
    content = remove_pandoc_underline_attributes(content)
    # Replace .emf image refs with placeholder so build doesn't fail (image-size doesn't support EMF)
    content = re.sub(r"\]\(([^)]+\.emf)\)", r"](/img/placeholder.png)", content, flags=re.IGNORECASE)
    if verbose:
        print("  Removing empty list items...")
    content = remove_empty_list_items(content)
    if verbose:
        print("  Merging list continuation lines...")
    content = merge_list_continuation_lines(content)
    if verbose:
        print("  Fixing Contacts section emails...")
    content = ensure_contacts_section_emails(content)
    if verbose:
        print("  Formatting doc title block (18pt / 24pt / 18pt)...")
    content = format_doc_title_block(content)
    if verbose:
        print("  Merging pipe table continuation rows...")
    content = merge_pipe_table_continuation_rows(content)
    if verbose:
        print("  Wrapping metadata table for AI-only visibility...")
    content = wrap_metadata_for_agents(content)
    content = fix_metadata_div_line_breaks(content)
    if verbose:
        print("  Demoting body headings (Introduction etc. one level smaller)...")
    content = demote_body_headings(content)
    if verbose:
        print("  Ensuring blank line before headings after tables...")
    content = ensure_blank_before_heading_after_table(content)
    if verbose:
        print("  Ensuring blank line before all headings (and standalone bold)...")
    content = ensure_blank_before_all_headings(content)
    if verbose:
        print("  Ensuring blank line after each image...")
    content = ensure_blank_after_images(content)
    return content


def ensure_blank_after_images(content):
    """Ensure at least one blank line after every markdown image so following text doesn't run into it."""
    lines = content.split("\n")
    result = []
    # Line that is only a markdown image: ![](url) or ![alt](url), optional leading/trailing whitespace
    image_line = re.compile(r"^\s*!\[[^\]]*\]\([^)]+\)\s*$")
    for i, line in enumerate(lines):
        result.append(line)
        if image_line.match(line.strip()) and i + 1 < len(lines):
            next_line = lines[i + 1].strip()
            if next_line != "" and result and result[-1].strip() != "":
                # Next line has content; ensure a blank after this image
                result.append("")
    return "\n".join(result)


def ensure_blank_before_all_headings(content):
    """Ensure at least one blank line before every ATX heading (## ###) and before
    standalone bold lines (**Heading**) so headings always start on a new line
    (e.g. after images or videos).
    """
    lines = content.split("\n")
    result = []
    atx_heading = re.compile(r"^#+\s+\S")
    standalone_bold = re.compile(r"^\s*\*\*[^*]+\*\*\s*$")  # line that is only **text**
    for i, line in enumerate(lines):
        stripped = line.strip()
        is_heading = atx_heading.match(stripped) or standalone_bold.match(stripped)
        if is_heading and result:
            # Ensure at least one blank line before this heading
            prev = result[-1].strip()
            if prev != "":
                result.append("")
        result.append(line)
    return "\n".join(result)


def ensure_blank_before_heading_after_table(content):
    """Ensure at least one blank line before any ATX heading (# ## ###) when the
    previous non-blank line looks like a table row or separator. Prevents the
    next section heading from being merged with the last table row (H1 styling).
    """
    lines = content.split("\n")
    result = []
    i = 0
    while i < len(lines):
        line = lines[i]
        result.append(line)
        stripped = line.strip()
        is_table_row = stripped.startswith("|") and stripped.endswith("|")
        is_table_sep = (
            bool(re.match(r"^[\s\-=]+$", stripped))
            and len(stripped) >= 2
            and "-" in stripped
        )
        if is_table_row or is_table_sep:
            # Look ahead: skip blank lines, see if next non-blank is ATX heading
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                result.append(lines[j])
                j += 1
            if j < len(lines) and re.match(r"^#+\s+\S", lines[j].strip()):
                # Next content is a heading; ensure at least two newlines before it
                # so the parser doesn't merge the heading with the last table row
                if result and result[-1].strip() != "":
                    result.append("")
                result.append("")
            i = j - 1  # advance to last blank we consumed (next iteration will be j)
        i += 1
    return "\n".join(result)


def remove_empty_list_items(content):
    """Remove markdown list lines that have no content. If an empty bullet is followed by
    a plain email or mailto link (Pandoc often puts link on next line), merge into one list item.
    """
    lines = content.split("\n")
    result = []
    i = 0
    email_or_mailto = re.compile(
        r"^\s*(\[.*?\]\(mailto:[^)]+\)|[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\s*$"
    )
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Empty list item: - or * with only whitespace
        if re.match(r"^[-*]\s*$", stripped) or re.match(r"^[-*]\s{2,}$", stripped):
            # Look at next non-blank line: if it's an email or mailto link, keep as one list item
            j = i + 1
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and email_or_mailto.match(lines[j].strip()):
                result.append(line.rstrip() + " " + lines[j].strip())
                i = j
                i += 1
                continue
            # Otherwise drop the empty bullet
            i += 1
            continue
        result.append(line)
        i += 1
    return "\n".join(result)


def fix_images_and_empty_lists(content):
    """Fix image paths and Pandoc size attributes, and remove empty list items. Used for one-off --fix-images-and-lists."""
    content = re.sub(r"!\[([^\]]*)\]\(docs/media/", r"![\1](media/", content)
    # MD/Asset/_pandoc_extract/DocName/media/... -> media/DocName/... (normalize to forward slashes)
    for asset in ("Thread", "IAI", "AOT", "A4E", "A4M"):
        content = re.sub(
            r"!\[([^\]]*)\]\(MD[/\\]" + asset + r"[/\\]_pandoc_extract[/\\]([^/\\]+)[/\\]media[/\\]([^)]+)\)",
            lambda m: f"![{m.group(1)}](media/{m.group(2)}/{m.group(3).replace(chr(92), '/')})",
            content,
        )
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]Thread[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]IAI[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]AOT[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]A4E[/\\]media/", r"![\1](media/", content)
    content = re.sub(r"!\[([^\]]*)\]\(MD[/\\]A4M[/\\]media/", r"![\1](media/", content)
    # Docusaurus resolves asset paths relative to the document only when they start with ./
    content = re.sub(r"\]\((media/[^)]+)\)", r"](./\1)", content)
    # Spaces in image URLs break Markdown parsing; encode as %20
    content = re.sub(
        r"\]\((\./media/[^)]+)\)",
        lambda m: "](" + m.group(1).replace(" ", "%20") + ")",
        content,
    )
    # Match Pandoc attribute block: optional \ before {; closing "} or "\}; replace with newline to preserve paragraph break
    content = re.sub(r"\\?\{width=\"[^\"]*\" height=\"[^\"]*\"\}\s*", "\n", content)
    content = re.sub(r"\\?\{width=\"[^\"]*\" height=\"[^\"]*\"\\\}\s*", "\n", content)
    # Ensure newline after image when it was glued to following text (e.g. ](media/x.png)Next sentence)
    content = re.sub(r"(\]\(media/[^)]+\.png\))([A-Za-z#])", r"\1\n\n\2", content)
    return remove_empty_list_items(content)


def clear_old_markdown(output_dir, preserve_intro=True):
    """Remove existing .md files in output_dir (optionally keep intro.md).
    Also remove the media/ folder so reconverted docs get fresh per-doc media (no stale shared images).
    """
    print("Clearing old markdown files...")
    out = Path(output_dir)
    if not out.exists():
        return
    for f in out.glob("*.md"):
        if preserve_intro and f.name == "intro.md":
            continue
        f.unlink()
        print(f"  Removed: {f.name}")
    media_dir = out / "media"
    if media_dir.exists():
        shutil.rmtree(media_dir)
        print("  Removed: media/ (stale images)")


def convert_docx_to_markdown(docx_file, input_dir, output_dir, dump_pandoc=False):
    """Convert one DOCX to Markdown. Returns True on success.
    Images are extracted to media/<doc_stem>/ so multiple docs in the same asset
    do not overwrite each other's images (e.g. image1.png from Doc A vs Doc B).
    If dump_pandoc is True, also write raw Pandoc output to <name>.pandoc_raw.md for debugging.
    """
    input_path = Path(input_dir) / docx_file
    output_filename = docx_file.replace(".docx", ".md")
    output_path = Path(output_dir) / output_filename
    doc_stem = output_path.stem  # e.g. AOT_Operations_Hierarchy_UI_Guide_Auriga
    # Extract to a doc-specific temp dir so we can move to media/<doc_stem>/ without overwriting other docs
    extract_dir = Path(output_dir) / "_pandoc_extract" / doc_stem
    extract_dir.mkdir(parents=True, exist_ok=True)
    final_media_dir = Path(output_dir) / "media" / doc_stem
    final_media_dir.mkdir(parents=True, exist_ok=True)

    try:
        print(f"\nConverting: {docx_file}")
        print("  Running pandoc...")
        subprocess.run(
            [
                "pandoc",
                str(input_path),
                "-f",
                "docx",
                "-t",
                "markdown",
                "--wrap=none",
                "--extract-media",
                str(extract_dir),
                "-o",
                str(output_path),
            ],
            capture_output=True,
            text=True,
            check=True,
        )

        with open(output_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Move extracted media from _pandoc_extract/<doc_stem>/media/* to media/<doc_stem>/
        pandoc_media = extract_dir / "media"
        if pandoc_media.exists():
            for f in pandoc_media.iterdir():
                if f.is_file():
                    shutil.move(str(f), str(final_media_dir / f.name))
            try:
                pandoc_media.rmdir()
            except OSError:
                pass
        try:
            extract_dir.rmdir()
        except OSError:
            pass
        try:
            (Path(output_dir) / "_pandoc_extract").rmdir()
        except OSError:
            pass

        # Pandoc may write image paths as _pandoc_extract/<doc_stem>/media/... (relative to output dir).
        # Rewrite those to media/<doc_stem>/... so they match where we moved the files.
        content = re.sub(
            r"!\[([^\]]*)\]\(_pandoc_extract[/\\]" + re.escape(doc_stem) + r"[/\\]media[/\\]([^)]+)\)",
            lambda m: f"![{m.group(1)}](media/{doc_stem}/{m.group(2).replace(chr(92), '/')})",
            content,
        )
        # Rewrite image paths in markdown: media/image1.png -> media/<doc_stem>/image1.png
        def _media_to_doc_media(m):
            path = m.group(2)
            if path.startswith("media/" + doc_stem + "/"):
                return m.group(0)  # already correct
            if path.startswith("media/"):
                path = path[6:]  # strip "media/"
            return f"![{m.group(1)}](media/{doc_stem}/{path})"
        content = re.sub(r"!\[([^\]]*)\]\((media/[^)]+)\)", _media_to_doc_media, content)

        if dump_pandoc:
            raw_path = output_path.parent / (output_path.stem + ".pandoc_raw.md")
            with open(raw_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Dumped raw Pandoc output to: {raw_path}")

        print("  Cleaning content...")
        cleaned = clean_markdown_content(content)

        if not cleaned.startswith("---"):
            doc_title = output_filename.replace(".md", "").replace("_", " ")
            frontmatter = f"""---
sidebar_position: 2
title: {doc_title}
hide_title: true
---

"""
            cleaned = frontmatter + cleaned

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print("  [OK] Converted successfully")
        if final_media_dir.exists() and any(final_media_dir.iterdir()):
            print(f"  [OK] Extracted images to media/{doc_stem}/")
        return True

    except subprocess.CalledProcessError as e:
        print(f"  [FAIL] Pandoc error: {e.stderr or e}")
        return False
    except FileNotFoundError:
        print("  [FAIL] Pandoc not found. Install from https://pandoc.org/installing.html")
        return False
    except Exception as e:
        print(f"  [FAIL] Error: {e}")
        return False


def discover_asset_folders(docx_base):
    """Return list of subfolder names under docx_base that contain at least one .docx."""
    docx_path = Path(docx_base)
    if not docx_path.is_dir():
        return []
    assets = []
    for entry in docx_path.iterdir():
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        docx_count = sum(
            1
            for f in entry.iterdir()
            if f.suffix.lower() == ".docx" and not f.name.startswith("~$")
        )
        if docx_count > 0:
            assets.append(entry.name)
    return sorted(assets)


def main():
    parser = argparse.ArgumentParser(
        description="Convert Word (.docx) files to Markdown for Docusaurus."
    )
    parser.add_argument(
        "input_dir",
        nargs="?",
        default=None,
        help="Directory containing .docx files (prompted if omitted)",
    )
    parser.add_argument(
        "output_dir",
        nargs="?",
        default=None,
        help="Output directory for .md files (default: docs)",
    )
    parser.add_argument(
        "--no-clear",
        action="store_true",
        help="Do not delete existing .md files before converting",
    )
    parser.add_argument(
        "--dump-pandoc",
        action="store_true",
        help="For each conversion, also write raw Pandoc output to <name>.pandoc_raw.md for debugging",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Discover all subfolders under DOCX, convert each to MD/<name> (use with DOCX/MD layout)",
    )
    parser.add_argument(
        "--docx-base",
        default="DOCX",
        help="Base folder for .docx assets when using --all (default: DOCX)",
    )
    parser.add_argument(
        "--md-base",
        default="MD",
        help="Base folder for .md output when using --all (default: MD)",
    )
    parser.add_argument(
        "--clean-toc-only",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Remove table of contents from existing .md files in DIR (default: MD); no conversion",
    )
    parser.add_argument(
        "--wrap-metadata-only",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Wrap metadata table in hidden div in existing .md files in DIR (default: MD); no conversion",
    )
    parser.add_argument(
        "--fix-table-headings",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Ensure blank line before headings that follow table rows/separators in existing .md (default: MD); no conversion",
    )
    parser.add_argument(
        "--convert-dash-tables",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Convert dash-style grid tables to pipe tables in existing .md (default: MD); no conversion",
    )
    parser.add_argument(
        "--fix-images-and-lists",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Fix image paths (MD/Thread/media → media), strip Pandoc size attrs, remove empty list items in existing .md (default: MD)",
    )
    parser.add_argument(
        "--fix-metadata-divs",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Ensure metadata <div>/</div> are on their own lines for MDX (default: MD); no conversion",
    )
    parser.add_argument(
        "--fix-emf-refs",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Replace .emf image refs with /img/placeholder.png in existing .md (default: MD); no conversion",
    )
    parser.add_argument(
        "--fix-malformed-links",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Fix markdown links with duplicate ](url) or trailing \\ in URL in existing .md (default: MD); no conversion",
    )
    parser.add_argument(
        "--fix-underline",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Remove Pandoc \\{.underline\\} and ]{.underline} from existing .md (default: MD); no conversion",
    )
    parser.add_argument(
        "--fix-blockquotes",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Restore blockquote > at line start (was escaped as &gt;) so images in blockquotes render (default: MD)",
    )
    parser.add_argument(
        "--fix-heading-blanks",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Ensure blank line before every ATX heading and standalone bold so headings start on a new line (default: MD)",
    )
    parser.add_argument(
        "--fix-image-linebreaks",
        metavar="DIR",
        nargs="?",
        const="MD",
        default=None,
        help="Ensure blank line after every image so following text doesn't run into it (default: MD)",
    )
    args = parser.parse_args()

    if args.fix_image_linebreaks is not None:
        md_root = os.path.expanduser(args.fix_image_linebreaks)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                new_content = ensure_blank_after_images(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Ensured blank after images in {fixed} file(s) under {md_root}")
        return 0

    if args.fix_heading_blanks is not None:
        md_root = os.path.expanduser(args.fix_heading_blanks)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                new_content = ensure_blank_before_all_headings(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Ensured blank before headings in {fixed} file(s) under {md_root}")
        return 0

    if args.fix_blockquotes is not None:
        md_root = os.path.expanduser(args.fix_blockquotes)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                if "&gt;" not in content:
                    continue
                new_content = restore_blockquote_angle(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Restored blockquote > in {fixed} file(s) under {md_root}")
        return 0

    if args.fix_underline is not None:
        md_root = os.path.expanduser(args.fix_underline)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                if ".underline" not in content:
                    continue
                new_content = remove_pandoc_underline_attributes(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Removed underline attributes in {fixed} file(s) under {md_root}")
        return 0

    if args.fix_malformed_links is not None:
        md_root = os.path.expanduser(args.fix_malformed_links)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                new_content = fix_malformed_markdown_links(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Fixed malformed links in {fixed} file(s) under {md_root}")
        return 0

    if args.fix_emf_refs is not None:
        md_root = os.path.expanduser(args.fix_emf_refs)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                if ".emf" not in content:
                    continue
                new_content = replace_emf_with_placeholder(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Replaced .emf refs with placeholder in {fixed} file(s) under {md_root}")
        return 0

    if args.fix_metadata_divs is not None:
        md_root = os.path.expanduser(args.fix_metadata_divs)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                if "metadata-for-agents" not in content:
                    continue
                new_content = fix_metadata_div_line_breaks(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Fixed metadata div line breaks in {fixed} file(s) under {md_root}")
        return 0

    if args.fix_images_and_lists is not None:
        md_root = os.path.expanduser(args.fix_images_and_lists)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                new_content = fix_images_and_empty_lists(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Fixed images and empty lists in {fixed} file(s) under {md_root}")
        return 0

    if args.convert_dash_tables is not None:
        md_root = os.path.expanduser(args.convert_dash_tables)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        converted = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                new_content = _convert_dash_grid_tables(content)
                new_content = ensure_blank_before_heading_after_table(new_content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Converted: {path}")
                    converted += 1
        print(f"Converted dash tables in {converted} file(s) under {md_root}")
        return 0

    if args.fix_table_headings is not None:
        md_root = os.path.expanduser(args.fix_table_headings)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        fixed = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                new_content = ensure_blank_before_heading_after_table(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Fixed: {path}")
                    fixed += 1
        print(f"Fixed table/heading spacing in {fixed} file(s) under {md_root}")
        return 0

    if args.wrap_metadata_only is not None:
        md_root = os.path.expanduser(args.wrap_metadata_only)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        wrapped = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                if 'class="metadata-for-agents"' in content:
                    continue
                new_content = wrap_metadata_for_agents(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Wrapped metadata: {path}")
                    wrapped += 1
        print(f"Wrapped metadata block in {wrapped} file(s) under {md_root}")
        return 0

    if args.clean_toc_only is not None:
        md_root = os.path.expanduser(args.clean_toc_only)
        if not os.path.isdir(md_root):
            print(f"Error: Directory not found: {md_root}")
            return 1
        cleaned = 0
        for root, _dirs, files in os.walk(md_root):
            for f in files:
                if not f.endswith(".md") or f.startswith("."):
                    continue
                path = os.path.join(root, f)
                with open(path, "r", encoding="utf-8") as fp:
                    content = fp.read()
                new_content = remove_table_of_contents(content)
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as fp:
                        fp.write(new_content)
                    print(f"  Removed ToC: {path}")
                    cleaned += 1
        print(f"Cleaned ToC from {cleaned} file(s) under {md_root}")
        return 0

    if args.all:
        docx_base = os.path.expanduser(args.docx_base)
        md_base = os.path.expanduser(args.md_base)
        if not os.path.isdir(docx_base):
            print(f"Error: DOCX base folder not found: {docx_base}")
            return 1
        assets = discover_asset_folders(docx_base)
        if not assets:
            print(f"No subfolders with .docx files found under {docx_base}")
            return 1
        print("=" * 70)
        print("WORD TO MARKDOWN CONVERTER (discovery mode)")
        print("=" * 70)
        print(f"DOCX base: {docx_base}")
        print(f"MD base:   {md_base}")
        print(f"Assets:    {', '.join(assets)}")
        print("=" * 70)
        total_ok = 0
        total_files = 0
        for name in assets:
            input_dir = os.path.join(docx_base, name)
            output_dir = os.path.join(md_base, name)
            os.makedirs(output_dir, exist_ok=True)
            if not args.no_clear:
                clear_old_markdown(output_dir)
            docx_files = [
                f
                for f in os.listdir(input_dir)
                if f.endswith(".docx") and not f.startswith("~$")
            ]
            total_files += len(docx_files)
            print(f"\n--- {name} ({len(docx_files)} file(s)) ---")
            for docx_file in docx_files:
                if convert_docx_to_markdown(
                    docx_file, input_dir, output_dir, dump_pandoc=getattr(args, "dump_pandoc", False)
                ):
                    total_ok += 1
        print("\n" + "=" * 70)
        print(f"SUCCESS: Converted {total_ok}/{total_files} documents across {len(assets)} asset(s)")
        print("=" * 70)
        return 0 if total_ok == total_files else 1

    input_dir = args.input_dir
    if input_dir is None:
        input_dir = input("Enter path to folder containing .docx files: ").strip()
        if not input_dir:
            input_dir = "."
    input_dir = os.path.expanduser(input_dir)

    output_dir = args.output_dir
    if output_dir is None:
        output_dir = input("Enter output folder for .md files [docs]: ").strip() or "docs"
    output_dir = os.path.expanduser(output_dir)

    if not os.path.isdir(input_dir):
        print(f"Error: Input directory not found: {input_dir}")
        return 1

    docx_files = [
        f
        for f in os.listdir(input_dir)
        if f.endswith(".docx") and not f.startswith("~$")
    ]
    if not docx_files:
        print(f"No .docx files found in {input_dir}")
        return 1

    print("=" * 70)
    print("WORD TO MARKDOWN CONVERTER")
    print("=" * 70)
    os.makedirs(output_dir, exist_ok=True)
    if not args.no_clear:
        clear_old_markdown(output_dir)
    print(f"\nFound {len(docx_files)} document(s) to convert")

    success = 0
    for docx_file in docx_files:
        if convert_docx_to_markdown(
            docx_file, input_dir, output_dir, dump_pandoc=getattr(args, "dump_pandoc", False)
        ):
            success += 1

    print("\n" + "=" * 70)
    if success == len(docx_files):
        print(f"SUCCESS: Converted {success}/{len(docx_files)} documents")
        print("\nNext steps: npm start (or npm run build)")
    else:
        print(f"Partial: {success}/{len(docx_files)} converted")
    print("=" * 70)
    return 0 if success == len(docx_files) else 1


if __name__ == "__main__":
    sys.exit(main())
