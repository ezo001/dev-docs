#!/usr/bin/env python3
"""
Post-process existing markdown files to escape curly braces for MDX compatibility
Run this on your already converted markdown files
"""

import os
import re
from pathlib import Path

DOCS_DIR = "docs"

def escape_curly_braces_in_file(file_path):
    """Escape curly braces in a markdown file except in code blocks"""
    print(f"Processing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    result = []
    in_code_block = False
    changes_made = 0
    
    for line in lines:
        original_line = line
        
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
                    # Count unescaped braces
                    before_count = parts[i].count('{') + parts[i].count('}')
                    # Escape curly braces that aren't already escaped
                    parts[i] = re.sub(r'(?<!\\)\{', r'\\{', parts[i])
                    parts[i] = re.sub(r'(?<!\\)\}', r'\\}', parts[i])
                    after_count = parts[i].count('\\{') + parts[i].count('\\}')
                    if before_count > 0:
                        changes_made += 1
            line = '`'.join(parts)
        
        result.append(line)
    
    if changes_made > 0:
        # Write back
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(result))
        print(f"  ✓ Fixed {changes_made} line(s) with curly braces")
        return True
    else:
        print(f"  - No changes needed")
        return False

def main():
    print("=" * 70)
    print("POST-PROCESSOR: Escape Curly Braces in Existing Markdown Files")
    print("=" * 70)
    
    if not os.path.exists(DOCS_DIR):
        print(f"\nError: {DOCS_DIR} directory not found!")
        return 1
    
    md_files = list(Path(DOCS_DIR).glob("*.md"))
    
    if not md_files:
        print(f"\nNo .md files found in {DOCS_DIR}/")
        return 1
    
    print(f"\nFound {len(md_files)} markdown file(s)")
    print()
    
    fixed_count = 0
    for md_file in md_files:
        if md_file.name == "intro.md":
            print(f"Skipping: {md_file.name}")
            continue
        
        if escape_curly_braces_in_file(md_file):
            fixed_count += 1
    
    print("\n" + "=" * 70)
    print(f"Processed {len(md_files)} files, modified {fixed_count} files")
    print("\nNext step: Run 'npm start' to test")
    print("=" * 70)
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())