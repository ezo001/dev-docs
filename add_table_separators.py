#!/usr/bin/env python3
"""
Add missing separator rows to markdown tables
"""

import re

def add_table_separators(content):
    """Add separator rows after table headers"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        result.append(line)
        
        # Check if this line looks like a table header (has pipes and bold text)
        if '|' in line and '**' in line and line.strip().startswith('|'):
            # Count the number of columns
            num_cols = line.count('|') - 1
            
            # Check if next line is NOT already a separator
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if not (next_line.startswith('|') and '---' in next_line):
                    # Add separator row
                    separator = '| ' + ' | '.join(['---'] * num_cols) + ' |'
                    result.append(separator)
        
        i += 1
    
    return '\n'.join(result)

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Adding table separator rows...")
    fixed_content = add_table_separators(content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! Table separators added.")