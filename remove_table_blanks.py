#!/usr/bin/env python3
"""
Remove blank lines within tables that break the table rendering
"""

import re

def remove_blank_lines_in_tables(content):
    """Remove blank lines between table rows"""
    lines = content.split('\n')
    result = []
    i = 0
    in_table = False
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this line is a table row
        if line.strip().startswith('|') and '|' in line.strip()[1:]:
            in_table = True
            result.append(line)
            i += 1
            continue
        
        # If we're in a table and hit a blank line, skip it
        if in_table and line.strip() == '':
            # Check if next line is also a table row
            if i + 1 < len(lines) and lines[i + 1].strip().startswith('|'):
                # Skip this blank line
                i += 1
                continue
            else:
                # End of table
                in_table = False
        else:
            in_table = False
        
        result.append(line)
        i += 1
    
    return '\n'.join(result)

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Removing blank lines within tables...")
    fixed_content = remove_blank_lines_in_tables(content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! Blank lines removed from tables.")