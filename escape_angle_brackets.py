import os
import re

def escape_angle_brackets(content):
    """
    Escape ALL angle brackets as HTML entities EXCEPT in code blocks.
    This prevents MDX from treating <UserID> etc. as JSX components.
    """
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    
    for line in lines:
        # Track code blocks
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        
        if in_code_block:
            fixed_lines.append(line)
            continue
        
        # Escape all angle brackets
        line = line.replace('<', '\\<')
        line = line.replace('>', '\\>')
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def process_all_files(docs_dir="docs"):
    """Process all markdown files."""
    print("=" * 70)
    print("Escaping all angle brackets with backslashes")
    print("=" * 70)
    
    fixed_count = 0
    total_count = 0
    
    for filename in os.listdir(docs_dir):
        if filename.endswith('.md'):
            total_count += 1
            filepath = os.path.join(docs_dir, filename)
            print(f"Processing: {filename}...", end=" ")
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                content = escape_angle_brackets(content)
                
                if content != original:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print("✓ Fixed")
                    fixed_count += 1
                else:
                    print("○ No changes")
            except Exception as e:
                print(f"✗ Error: {e}")
    
    print("=" * 70)
    print(f"Fixed {fixed_count} out of {total_count} files")
    print("=" * 70)

if __name__ == "__main__":
    process_all_files()