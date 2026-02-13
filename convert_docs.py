#!/usr/bin/env python3
"""
IMPROVED Word to Markdown Converter for Docusaurus
Now escapes curly braces instead of removing them
"""

import os
import subprocess
import sys
import re
from pathlib import Path

DOCS_DIR = "docs"
INPUT_DIR = "."
OUTPUT_DIR = DOCS_DIR

def clear_old_markdown():
    """Remove old markdown files"""
    print("Clearing old markdown files...")
    if os.path.exists(OUTPUT_DIR):
        for file in Path(OUTPUT_DIR).glob("*.md"):
            if file.name != "intro.md":
                file.unlink()
                print(f"  Removed: {file.name}")

def parse_grid_table(table_lines):
    """Parse grid table and convert to pipe table with all cells on one line"""
    data_rows = []
    current_row_cells = []
    
    for line in table_lines:
        stripped = line.strip()
        
        # Skip separator lines
        if not stripped.startswith('|') or all(c in '|+- =' for c in stripped):
            continue
        
        # This is a data line - extract cells
        cells = stripped.split('|')[1:-1]
        
        # Check if this is a new row (starts with |) or continuation
        if stripped.startswith('|'):
            # If we have accumulated cells, save them as a row
            if current_row_cells:
                data_rows.append(current_row_cells)
                current_row_cells = []
            
            # Start new row
            current_row_cells = [cell.strip() for cell in cells]
        else:
            # Continuation of previous row - append to existing cells
            for i, cell in enumerate(cells):
                if i < len(current_row_cells):
                    current_row_cells[i] += ' ' + cell.strip()
    
    # Don't forget the last row
    if current_row_cells:
        data_rows.append(current_row_cells)
    
    if not data_rows:
        return []
    
    # Clean cells and create pipe rows
    pipe_rows = []
    for cells in data_rows:
        cleaned_cells = []
        for cell in cells:
            # Remove HTML tags
            cell = re.sub(r'<[^>]+>', '', cell)
            # Remove extra whitespace
            cell = ' '.join(cell.split())
            cleaned_cells.append(cell)
        
        if any(cell for cell in cleaned_cells):
            pipe_rows.append('| ' + ' | '.join(cleaned_cells) + ' |')
    
    # Add separator after first row (header)
    if len(pipe_rows) > 1:
        num_cols = pipe_rows[0].count('|') - 1
        separator = '| ' + ' | '.join(['---'] * num_cols) + ' |'
        pipe_rows.insert(1, separator)
    
    return pipe_rows

def convert_grid_tables_to_pipe(content):
    """Convert all grid tables to pipe tables"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Detect start of grid table
        if re.match(r'^\s*\+[-=]+\+', line):
            # Collect entire table
            table_lines = []
            while i < len(lines) and (lines[i].strip().startswith('+') or lines[i].strip().startswith('|')):
                table_lines.append(lines[i])
                i += 1
            
            # Convert and add
            pipe_table = parse_grid_table(table_lines)
            if pipe_table:
                result.append('')  # Blank line before table
                result.extend(pipe_table)
                result.append('')  # Blank line after table
            continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def escape_curly_braces_safe(content):
    """Escape curly braces except in code blocks and inline code"""
    lines = content.split('\n')
    result = []
    in_code_block = False
    
    for line in lines:
        # Toggle code block state
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(line)
            continue
        
        if not in_code_block:
            # Don't escape inside inline code (`...`)
            # Split by backticks and only escape outside of them
            parts = line.split('`')
            for i in range(len(parts)):
                if i % 2 == 0:  # Outside inline code
                    # Escape curly braces
                    parts[i] = parts[i].replace('{', '\\{').replace('}', '\\}')
            line = '`'.join(parts)
        
        result.append(line)
    
    return '\n'.join(result)

def clean_markdown_content(content):
    """Complete cleanup of markdown"""
    
    # 1. Convert grid tables to pipe tables
    print("  Converting grid tables...")
    content = convert_grid_tables_to_pipe(content)
    
    # 2. Remove HTML tags
    print("  Removing HTML tags...")
    content = re.sub(r'<[^>]+>', '', content)
    
    # 3. Escape curly braces (except in code) - CHANGED FROM REMOVE
    print("  Escaping curly braces...")
    content = escape_curly_braces_safe(content)
    
    # 4. Fix image paths
    print("  Fixing image paths...")
    content = re.sub(r'!\[([^\]]*)\]\(docs/media/', r'![\1](media/', content)
    
    # 5. Remove underline tags from links
    content = re.sub(r'\[<u>([^<]+)</u>\]', r'[\1]', content)
    
    # 6. Fix common MDX issues
    print("  Fixing MDX issues...")
    # Fix lazy lines in lists - ensure proper indentation
    lines = content.split('\n')
    fixed_lines = []
    in_list = False
    for line in lines:
        if re.match(r'^\s*[-*+]\s', line):
            in_list = True
        elif in_list and line.strip() and not line.startswith(' '):
            in_list = False
        fixed_lines.append(line)
    content = '\n'.join(fixed_lines)
    
    return content

def convert_docx_to_markdown(docx_file):
    """Convert DOCX to Markdown"""
    try:
        input_path = Path(INPUT_DIR) / docx_file
        output_filename = docx_file.replace('.docx', '.md')
        output_path = Path(OUTPUT_DIR) / output_filename
        
        media_dir = Path(OUTPUT_DIR) / 'media'
        media_dir.mkdir(exist_ok=True)
        
        print(f"\nConverting: {docx_file}")
        print("  Running pandoc...")
        
        # Use plain markdown (creates grid tables)
        result = subprocess.run(
            [
                'pandoc',
                str(input_path),
                '-f', 'docx',
                '-t', 'markdown',
                '--wrap=none',
                '--extract-media', str(OUTPUT_DIR),
                '-o', str(output_path)
            ],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Read and clean
        with open(output_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        print("  Cleaning content...")
        cleaned_content = clean_markdown_content(content)
        
        # Add frontmatter
        if not cleaned_content.startswith('---'):
            doc_title = output_filename.replace('.md', '').replace('_', ' ')
            frontmatter = f"""---
sidebar_position: 2
title: {doc_title}
---

"""
            cleaned_content = frontmatter + cleaned_content
        
        # Write back
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cleaned_content)
        
        print(f"  ✓ Converted successfully")
        
        if media_dir.exists() and any(media_dir.iterdir()):
            print(f"  ✓ Extracted images to media/")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 70)
    print("IMPROVED WORD TO MARKDOWN CONVERTER")
    print("Now escaping curly braces instead of removing them")
    print("=" * 70)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_old_markdown()
    
    docx_files = [f for f in os.listdir(INPUT_DIR) 
                  if f.endswith('.docx') and not f.startswith('~$')]
    
    if not docx_files:
        print("\nNo .docx files found in current directory")
        return 1
    
    print(f"\nFound {len(docx_files)} document(s) to convert")
    
    success_count = 0
    for docx_file in docx_files:
        if convert_docx_to_markdown(docx_file):
            success_count += 1
    
    print("\n" + "=" * 70)
    if success_count == len(docx_files):
        print(f"SUCCESS! Converted {success_count}/{len(docx_files)} documents")
        print("\nNext steps:")
        print("  1. Handle .emf images (see below)")
        print("  2. Run: npm start")
        print("  3. Fix any remaining errors manually")
        print("\n.EMF Image Issue:")
        print("  Add to docusaurus.config.js to ignore them temporarily:")
        print("  markdown: { hooks: { onBrokenMarkdownImages: (path) => {")
        print("    if (path.endsWith('.emf')) return 'pathname://placeholder.png';")
        print("  }}}")
    else:
        print(f"Partial success: {success_count}/{len(docx_files)} converted")
    print("=" * 70)
    
    return 0 if success_count == len(docx_files) else 1

if __name__ == "__main__":
    sys.exit(main())