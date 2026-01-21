#!/usr/bin/env python3
"""
Fix malformed tables by merging consecutive pipe lines into proper rows
"""

import re

def fix_malformed_tables(content):
    """Merge consecutive lines starting with | into proper table rows"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Check if this line starts with a pipe (potential table cell)
        if line.startswith('| '):
            # Collect all consecutive pipe lines
            row_cells = []
            while i < len(lines) and lines[i].strip().startswith('| '):
                cell = lines[i].strip()[2:]  # Remove '| ' prefix
                if cell:  # Only add non-empty cells
                    row_cells.append(cell)
                i += 1
            
            # Create a proper table row
            if row_cells:
                table_row = '| ' + ' | '.join(row_cells) + ' |'
                result.append(table_row)
                
                # Check if this looks like a header (contains ** bold markers)
                if '**' in table_row and len(result) > 0:
                    # Check if next row is also a table row (not already added separator)
                    if i < len(lines) and lines[i].strip().startswith('| '):
                        # Add separator row
                        separator = '| ' + ' | '.join(['---'] * len(row_cells)) + ' |'
                        result.append(separator)
            continue
        
        result.append(lines[i])
        i += 1
    
    return '\n'.join(result)

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Fixing malformed tables...")
    fixed_content = fix_malformed_tables(content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! Tables should now be properly formatted.")