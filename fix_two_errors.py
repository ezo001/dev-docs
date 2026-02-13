#!/usr/bin/env python3
"""
Fix specific MDX errors in problematic files
"""

import re
from pathlib import Path

DOCS_DIR = "docs"

def fix_generic_scheduler(file_path):
    """Fix AOT_Generic_Scheduler_Technical_Overview_Auriga.md - line 255, column 26"""
    print(f"\nFixing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Check around line 255
    if len(lines) >= 255:
        print(f"  Line 255: {lines[254][:100]}...")
        
        # Look for unescaped { without closing }
        # Common issue: something like "value: {" without closing brace
        for i in range(max(0, 254-5), min(len(lines), 254+5)):
            line = lines[i]
            # Count unescaped braces
            open_braces = len(re.findall(r'(?<!\\)\{', line))
            close_braces = len(re.findall(r'(?<!\\)\}', line))
            
            if open_braces != close_braces:
                print(f"  Line {i+1} has unbalanced braces: {open_braces} open, {close_braces} close")
                print(f"    Content: {line[:100]}")
                
                # Fix by escaping all braces in this line (if not in code block)
                if not line.strip().startswith('```') and '`' not in line:
                    original = line
                    line = line.replace('{', '\\{').replace('}', '\\}')
                    # Remove double escaping
                    line = line.replace('\\\\{', '\\{').replace('\\\\}', '\\}')
                    lines[i] = line
                    print(f"    Fixed to: {line[:100]}")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("  ✓ Fixed")

def fix_mfe_development(file_path):
    """Fix AOT_Micro_Front_End_MFE_Development_Guide_Auriga.md - line 491, column 9"""
    print(f"\nFixing: {file_path.name}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Check around line 491
    if len(lines) >= 491:
        print(f"  Line 491: {lines[490][:100]}...")
        
        # This is an "import/exports" error - likely has something that looks like:
        # import or export statement that's not valid JS
        for i in range(max(0, 490-5), min(len(lines), 490+5)):
            line = lines[i]
            
            # Check if line starts with import or export (MDX thinks it's JS)
            if line.strip().startswith(('import ', 'export ', 'import{', 'export{')):
                print(f"  Line {i+1} starts with import/export:")
                print(f"    Content: {line[:100]}")
                
                # Escape it or wrap in code block
                if not lines[i-1].strip().startswith('```'):
                    # Add code fence
                    lines[i] = '`' + line.strip() + '`\n'
                    print(f"    Fixed to: {lines[i][:100]}")
            
            # Also check for unescaped braces
            open_braces = len(re.findall(r'(?<!\\)\{', line))
            close_braces = len(re.findall(r'(?<!\\)\}', line))
            
            if open_braces != close_braces:
                print(f"  Line {i+1} has unbalanced braces")
                if not line.strip().startswith('```') and '`' not in line:
                    original = line
                    line = line.replace('{', '\\{').replace('}', '\\}')
                    line = line.replace('\\\\{', '\\{').replace('\\\\}', '\\}')
                    lines[i] = line
                    print(f"    Fixed braces")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("  ✓ Fixed")

def main():
    print("=" * 70)
    print("TARGETED MDX ERROR FIXER")
    print("=" * 70)
    
    docs_path = Path(DOCS_DIR)
    
    # Fix specific files
    file1 = docs_path / "AOT_Generic_Scheduler_Technical_Overview_Auriga.md"
    if file1.exists():
        fix_generic_scheduler(file1)
    else:
        print(f"\n✗ File not found: {file1}")
    
    file2 = docs_path / "AOT_Micro_Front_End_MFE_Development_Guide_Auriga.md"
    if file2.exists():
        fix_mfe_development(file2)
    else:
        print(f"\n✗ File not found: {file2}")
    
    print("\n" + "=" * 70)
    print("Done! Run 'npm start' to test")
    print("=" * 70)

if __name__ == "__main__":
    import sys
    sys.exit(main())