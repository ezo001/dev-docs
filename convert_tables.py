#!/usr/bin/env python3
"""
Convert grid tables to pipe tables and clean HTML tags
"""

import re

def convert_grid_tables_to_pipe(content):
    """Convert Pandoc grid tables to pipe tables"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is the start of a grid table (line with +---+)
        if re.match(r'^\s*\+[-=]+\+', line):
            # Collect all table lines
            table_lines = []
            while i < len(lines) and (lines[i].strip().startswith('+') or lines[i].strip().startswith('|')):
                table_lines.append(lines[i])
                i += 1
            
            # Parse and convert the grid table
            pipe_table = parse_grid_table(table_lines)
            result.extend(pipe_table)
            continue
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

def parse_grid_table(table_lines):
    """Parse a grid table and convert to pipe table"""
    # Extract data rows (lines starting with |, not separators)
    data_rows = [line for line in table_lines if line.strip().startswith('|') and '---' not in line and '===' not in line]
    
    if not data_rows:
        return []
    
    pipe_rows = []
    for row in data_rows:
        # Split by | and clean up
        cells = row.split('|')[1:-1]  # Remove first and last empty elements
        
        # Clean each cell
        cleaned_cells = []
        for cell in cells:
            cell = cell.strip()
            # Remove HTML tags
            cell = re.sub(r'<[^>]+>', '', cell)
            cleaned_cells.append(cell)
        
        # Only add rows with content
        if any(cell for cell in cleaned_cells):
            pipe_rows.append('| ' + ' | '.join(cleaned_cells) + ' |')
    
    # Add separator after first row (header)
    if len(pipe_rows) > 1:
        num_cols = pipe_rows[0].count('|') - 1
        separator = '| ' + ' | '.join(['---'] * num_cols) + ' |'
        pipe_rows.insert(1, separator)
    
    return [''] + pipe_rows + ['']

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Converting grid tables to pipe tables...")
    fixed_content = convert_grid_tables_to_pipe(content)
    
    print("Removing any remaining HTML tags...")
    fixed_content = re.sub(r'<[^>]+>', '', fixed_content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! Tables converted to pipe format.")