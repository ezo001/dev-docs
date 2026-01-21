#!/usr/bin/env python3
"""
Fix wrapped table rows by joining them into single lines
"""

import re

def unwrap_table_rows(content):
    """Remove line breaks within table cells"""
    
    # Pattern: table row that doesn't end with |
    # followed by text that ends with |
    # This captures wrapped table rows
    
    # Keep processing until no more wrapped rows found
    max_iterations = 100
    iteration = 0
    
    while iteration < max_iterations:
        # Find pattern: | ... (no ending |) \n text ending with |
        pattern = r'(\|[^|\n]+\|[^|\n]+)\n([^|\n]+\|)'
        
        new_content = re.sub(pattern, r'\1 \2', content)
        
        # If nothing changed, we're done
        if new_content == content:
            break
            
        content = new_content
        iteration += 1
    
    return content

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Unwrapping table rows...")
    fixed_content = unwrap_table_rows(content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! All table rows should now be on single lines.")