import os
import re

def wrap_problematic_content_in_code(content):
    """
    Wrap problematic patterns in backticks outside code blocks.
    This includes: curly braces, backslashes with angle brackets, equals with angle brackets, etc.
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
        
        # Fix 1: Wrap unmatched curly braces in backticks
        open_count = line.count('{')
        close_count = line.count('}')
        if open_count != close_count:
            line = re.sub(r'(?<!`)\{', r'`{`', line)
            line = re.sub(r'(?<!`)\}', r'`}`', line)
        
        # Fix 2: Wrap backslash-angle brackets patterns like \< or \>
        line = re.sub(r'\\<', r'`\\<`', line)
        line = re.sub(r'\\>', r'`\\>`', line)
        
        # Fix 3: Replace smart quotes with regular quotes
        line = line.replace(''', "'")
        line = line.replace(''', "'")
        line = line.replace('"', '"')
        line = line.replace('"', '"')
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def remove_image_references(content):
    """Remove markdown image references."""
    # Pattern: ![alt text](media/image12.png)
    content = re.sub(r'!\[([^\]]*)\]\(media/[^\)]+\)', r'*[Image: \1]*', content)
    return content

def process_all_files(docs_dir="docs"):
    """Process all markdown files."""
    print("=" * 70)
    print("Final fixes: curly braces, backslashes, quotes, images")
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
                content = wrap_problematic_content_in_code(content)
                content = remove_image_references(content)
                
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