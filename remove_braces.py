#!/usr/bin/env python3
"""
Remove all curly braces that aren't part of valid MDX
"""

import re

def remove_curly_braces(content):
    """Remove or escape curly braces"""
    
    # Remove {.class}, {#id}, {width=...}, etc
    content = re.sub(r'\{[^}]*\}', '', content)
    
    return content

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Removing curly braces...")
    fixed_content = remove_curly_braces(content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! All curly braces removed.")