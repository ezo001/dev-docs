#!/usr/bin/env python3
"""
Comprehensive Word to Markdown converter for Docusaurus
Handles all table conversions and cleanup in one go
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

def convert_grid_tables_to_pipe(content):
    """Convert Pandoc grid tables to pipe tables"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a grid table separator line
        if re.match(r'^\s*\+[-=]+\+', line):
            # Collect the entire grid table
            table_lines = []
            while i < len(lines) and (lines[i].strip().startswith('+') or lines[i].strip().startswith('|')):
                table_lines.append(lines[i])
                i += 1
            
            # Parse the grid table
            pipe_table = parse_grid_table(table_lines)
            result.extend(pipe_table)
            continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def parse_grid_table(table_lines):
    """Parse grid table and convert to pipe table"""
    # Extract data rows (lines with |, not separators)
    data_rows = []
    for line in table_lines:
        stripped = line.strip()
        if stripped.startswith('|') and not all(c in '|+- =' for c in stripped):
            data_rows.append(line)
    
    if not data_rows:
        return []
    
    pipe_rows = []
    for row in data_rows:
        # Split by | and clean cells
        cells = row.split('|')[1:-1]
        cleaned_cells = []
        for cell in cells:
            cell = cell.strip()
            # Remove HTML tags
            cell = re.sub(r'<[^>]+>', '', cell)
            # Join multi-line cells
            cell = ' '.join(cell.split())
            cleaned_cells.append(cell)
        
        if any(cell for cell in cleaned_cells):
            pipe_rows.append('| ' + ' | '.join(cleaned_cells) + ' |')
    
    # Add separator after first row
    if len(pipe_rows) > 1:
        num_cols = pipe_rows[0].count('|') - 1
        separator = '| ' + ' | '.join(['---'] * num_cols) + ' |'
        pipe_rows.insert(1, separator)
    
    return [''] + pipe_rows + ['']

def clean_markdown_content(content):
    """Clean up markdown for MDX compatibility"""
    
    # Convert grid tables first
    content = convert_grid_tables_to_pipe(content)
    
    # Remove all HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    
    # Remove Pandoc attributes
    content = re.sub(r'\{[.#][^}]+\}', '', content)
    content = re.sub(r'\[([^\]]+)\]\{[^}]+\}(\([^)]+\))', r'[\1]\2', content)
    
    # Fix image paths
    content = re.sub(r'!\[([^\]]*)\]\(docs/media/', r'![\1](media/', content)
    
    return content

def convert_docx_to_markdown(docx_file):
    """Convert DOCX to Markdown"""
    try:
        input_path = Path(INPUT_DIR) / docx_file
        output_filename = docx_file.replace('.docx', '.md')
        output_path = Path(OUTPUT_DIR) / output_filename
        
        media_dir = Path(OUTPUT_DIR) / 'media'
        media_dir.mkdir(exist_ok=True)
        
        print(f"Converting: {docx_file}")
        
        # Use plain markdown format
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
        
        print(f"  ✓ Converted to {output_filename}")
        
        if media_dir.exists() and any(media_dir.iterdir()):
            print(f"  ✓ Extracted images")
        
        return True
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def main():
    print("=" * 70)
    print("CONVERTING WORD TO MARKDOWN")
    print("=" * 70)
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_old_markdown()
    
    docx_files = [f for f in os.listdir(INPUT_DIR) 
                  if f.endswith('.docx') and not f.startswith('~$')]
    
    if not docx_files:
        print("No .docx files found")
        return 1
    
    print(f"Found {len(docx_files)} documents")
    
    success_count = 0
    for docx_file in docx_files:
        if convert_docx_to_markdown(docx_file):
            success_count += 1
    
    print("=" * 70)
    print(f"SUCCESS: {success_count}/{len(docx_files)}")
    print("=" * 70)
    return 0

if __name__ == "__main__":
    sys.exit(main())