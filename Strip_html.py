#!/usr/bin/env python3
"""
Remove all HTML tags from a markdown file
"""

import re
import sys

def remove_all_html_tags(content):
    """Remove all HTML tags"""
    # Remove all HTML tags
    content = re.sub(r'<[^>]+>', '', content)
    return content

if __name__ == "__main__":
    filepath = "docs/AOT_Architecture_Azure_Auriga.md"
    
    print(f"Reading {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("Removing all HTML tags...")
    fixed_content = remove_all_html_tags(content)
    
    print(f"Writing back to {filepath}...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print("Done! All HTML tags removed.")