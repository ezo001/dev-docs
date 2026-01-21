#!/usr/bin/env python3
"""
Convert Word documents to Markdown with proper cleanup for Docusaurus/MDX compatibility
"""

import os
import subprocess
import sys
import re
from pathlib import Path

# Configuration
DOCS_DIR = "docs"
INPUT_DIR = "."  # Current directory for .docx files
OUTPUT_DIR = DOCS_DIR

def clear_old_markdown():
    """Remove old markdown files to ensure clean conversion"""
    print("Clearing old markdown files...")
    if os.path.exists(OUTPUT_DIR):
        for file in Path(OUTPUT_DIR).glob("*.md"):
            if file.name != "intro.md":  # Preserve intro.md if it exists
                file.unlink()
                print(f"  Removed: {file.name}")

def clean_markdown_content(content):
    """
    Clean up markdown content to be MDX-compatible
    """
    # Remove Pandoc-style formatting attributes like {.underline}, {#id}, {.class}
    # This regex matches [text]{.anything} and converts it to [text]
    content = re.sub(r'\[([^\]]+)\]\{[^}]+\}(\([^)]+\))', r'[\1]\2', content)
    
    # Remove image width/height attributes: (image.png){width="..." height="..."}
    # This matches the pattern and removes everything in curly braces after image paths
    content = re.sub(r'(\!\[[^\]]*\]\([^)]+\))\{[^}]+\}', r'\1', content)
    
    # Also handle standalone {.class} or {#id} that aren't part of links or images
    content = re.sub(r'\{[.#][^}]+\}', '', content)
    
    # Remove any remaining width/height attributes that might be standalone
    content = re.sub(r'\{width="[^"]*"\s*height="[^"]*"\}', '', content)
    content = re.sub(r'\{height="[^"]*"\s*width="[^"]*"\}', '', content)
    
    # Fix image paths - remove 'docs/' prefix since markdown files are already in docs/
    content = re.sub(r'!\[([^\]]*)\]\(docs/media/', r'![\1](media/', content)
    
    # Convert HTML img tags to markdown format
    # Pattern: <img src="path" ... alt="text" /> -> ![text](path)
    def img_to_markdown(match):
        src = re.search(r'src="([^"]+)"', match.group(0))
        alt = re.search(r'alt="([^"]+)"', match.group(0))
        if src:
            src_path = src.group(1).replace('docs/media/', 'media/')
            alt_text = alt.group(1) if alt else ''
            return f'![{alt_text}]({src_path})'
        return match.group(0)
    
    content = re.sub(r'<img[^>]+/?>', img_to_markdown, content)
    
    # Convert HTML img tags to markdown FIRST (before trying to clean attributes)
    # This is more reliable than trying to clean the HTML
    def img_to_markdown(match):
        img_tag = match.group(0)
        src_match = re.search(r'src="([^"]*)"', img_tag)
        alt_match = re.search(r'alt="([^"]*)"', img_tag)
        if src_match:
            src = src_match.group(1)
            alt = alt_match.group(1) if alt_match else ''
            # Fix the docs/ prefix if present
            src = src.replace('docs/media/', 'media/')
            return f'![{alt}]({src})'
        return ''  # If we can't parse it, just remove it
    
    content = re.sub(r'<img[^>]*/?>', img_to_markdown, content)
    
    # Remove HTML table tags that cause MDX errors
    # But DO NOT remove the content - convert to plain text/markdown
    # Remove only the tags, keeping the text content
    content = re.sub(r'</?table[^>]*>\n?', '\n', content)
    content = re.sub(r'</?thead[^>]*>\n?', '\n', content)
    content = re.sub(r'</?tbody[^>]*>\n?', '\n', content)
    content = re.sub(r'<tr[^>]*>\n?', '\n', content)
    content = re.sub(r'</tr>\n?', '\n', content)
    content = re.sub(r'<th[^>]*>', '| **', content)
    content = re.sub(r'</th>', '** ', content)
    content = re.sub(r'<td[^>]*>', '| ', content)
    content = re.sub(r'</td>', ' ', content)
    content = re.sub(r'</?colgroup[^>]*>', '', content)
    content = re.sub(r'<col[^>]*/?>', '', content)
    
    # Remove HTML list tags that cause MDX errors
    content = re.sub(r'</?ol[^>]*>', '', content)
    content = re.sub(r'</?ul[^>]*>', '', content)
    content = re.sub(r'</?li[^>]*>', '', content)
    content = re.sub(r'</?dl[^>]*>', '', content)
    content = re.sub(r'</?dt[^>]*>', '', content)
    content = re.sub(r'</?dd[^>]*>', '', content)
    
    # Remove inline style attributes that cause React errors
    content = re.sub(r'\s+style="[^"]*"', '', content)
    content = re.sub(r"\s+style='[^']*'", '', content)
    
    # Remove other problematic HTML attributes
    content = re.sub(r'\s+class="[^"]*"', '', content)
    content = re.sub(r'\s+id="[^"]*"', '', content)
    
    # Clean up excessive pipes and whitespace from HTML table conversion
    content = re.sub(r'\|\s*\|', '|', content)
    content = re.sub(r'\n\s*\|\s*\n', '\n', content)
    
    # Fix markdown tables - ensure they have proper header separators
    # A proper markdown table needs: header row, separator row (|---|---|), data rows
    def fix_tables(text):
        lines = text.split('\n')
        result = []
        i = 0
        while i < len(lines):
            line = lines[i]
            # Check if this looks like a table header (starts with |, has multiple |)
            if line.strip().startswith('|') and line.count('|') >= 3:
                # Check if next line is also a table row (not a separator)
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    # If next line is a table row but NOT a separator, we need to add one
                    if (next_line.startswith('|') and 
                        not re.match(r'\|[\s\-:]+\|', next_line) and
                        '---' not in next_line):
                        # This is likely a table without separator
                        # Add the current header line
                        result.append(line)
                        # Generate separator based on number of columns
                        cols = line.count('|') - 1
                        separator = '|' + ' --- |' * cols
                        result.append(separator)
                        i += 1
                        continue
            result.append(line)
            i += 1
        return '\n'.join(result)
    
    content = fix_tables(content)
    
    # Escape curly braces that are not part of JSX/MDX syntax
    # This is a simple approach - may need refinement for complex cases
    lines = content.split('\n')
    cleaned_lines = []
    in_code_block = False
    
    for line in lines:
        # Track code blocks to avoid escaping braces inside them
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            cleaned_lines.append(line)
            continue
        
        if not in_code_block:
            # Don't escape braces that are already part of valid MDX/JSX
            # This is a basic implementation
            if '{' in line or '}' in line:
                # Skip lines that look like they contain JSX/MDX components
                if not (line.strip().startswith('<') or 'import ' in line or 'export ' in line):
                    # For safety, only escape standalone braces not in code
                    # This might need adjustment based on your content
                    pass  # For now, we'll rely on the regex cleanup above
        
        cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines)

def convert_docx_to_markdown(docx_file):
    """Convert a single DOCX file to Markdown using pandoc"""
    try:
        input_path = Path(INPUT_DIR) / docx_file
        output_filename = docx_file.replace('.docx', '.md')
        output_path = Path(OUTPUT_DIR) / output_filename
        
        # Create media directory for images
        media_dir = Path(OUTPUT_DIR) / 'media'
        media_dir.mkdir(exist_ok=True)
        
        print(f"Converting: {docx_file}")
        
        # Run pandoc conversion with image extraction
        result = subprocess.run(
            [
                'pandoc',
                str(input_path),
                '-f', 'docx',
                '-t', 'markdown_strict+pipe_tables+strikeout',  # Basic markdown with pipe tables
                '--wrap=none',  # Don't wrap lines
                '--extract-media', str(OUTPUT_DIR),  # Extract images to docs folder
                '-o', str(output_path)
            ],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Read the generated markdown
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean the content
        cleaned_content = clean_markdown_content(content)
        
        # Add frontmatter if not present
        if not cleaned_content.startswith('---'):
            # Extract title from filename or first heading
            doc_title = output_filename.replace('.md', '').replace('_', ' ')
            frontmatter = f"""---
sidebar_position: 2
title: {doc_title}
---

"""
            cleaned_content = frontmatter + cleaned_content
        
        # Write back the cleaned content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"  ✓ Converted to {output_filename}")
        
        # Check if images were extracted
        if media_dir.exists() and any(media_dir.iterdir()):
            print(f"  ✓ Extracted images to {media_dir}")
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Error converting {docx_file}")
        print(f"    {e.stderr}")
        return False
    except Exception as e:
        print(f"  ✗ Unexpected error with {docx_file}: {e}")
        return False

def main():
    """Main conversion process"""
    print("=" * 70)
    print("CONVERTING WORD DOCUMENTS TO MARKDOWN")
    print("=" * 70)
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Clear old markdown files
    clear_old_markdown()
    
    # Find all .docx files
    docx_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.docx') and not f.startswith('~$')]
    
    if not docx_files:
        print("No .docx files found in current directory")
        return 1
    
    print(f"Found {len(docx_files)} documents to convert")
    
    # Convert each file
    success_count = 0
    for docx_file in docx_files:
        if convert_docx_to_markdown(docx_file):
            success_count += 1
    
    # Print summary
    print("=" * 70)
    print("CONVERSION COMPLETE")
    print(f"  Success: {success_count}/{len(docx_files)}")
    print(f"  Failed: {len(docx_files) - success_count}/{len(docx_files)}")
    print("=" * 70)
    
    if success_count == len(docx_files):
        print("Next steps:")
        print("1. Run: npm run build")
        print("2. If successful:")
        print("   git add .")
        print("   git commit -m \"Updated documentation with clean conversions\"")
        print("   git push")
    else:
        print("\n⚠ Some conversions failed. Please review the errors above.")
        return 1
    
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())