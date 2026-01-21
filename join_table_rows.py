#!/usr/bin/env python3
"""
Join wrapped table rows into single lines
"""

import re

def join_wrapped_table_rows(content):
    """Join table rows that are wrapped across multiple lines"""
    lines = content.split('\n')
    result = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check if this is a table row (starts with |)
        if line.strip().startswith('|') and not line.strip().endswith('|'):
            # This row doesn't end with |, it's wrapped
            # Collect continuation lines
            full_row = line.rstrip()
            i += 1
            
            # Keep adding lines until we find one that ends with |
            while i < len(lines):
                next_line = lines[i].strip()
                
                # If next line starts with |, it's a new row, stop
                if next_line.startswith('|'):
                    break
                
                # If next line ends with |, it's the continuation we need
                if next_line.endswith('|'):
                    full_row += ' ' + next_line
                    i += 1
                    break
                
                # Otherwise keep collecting
                full_row += ' ' + next_line
                i += 1
            
            result.append(full_row)
        else:
            result.append(line)
            i += 1
    
    return '\n'.join(result)

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Joining wrapped table rows...")
    fixed_content = join_wrapped_table_rows(content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! Table rows joined.")