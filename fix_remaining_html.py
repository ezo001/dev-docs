import os
import re

def fix_remaining_html_issues(content):
    """
    Fix the specific pattern: "&gt; which should be ">
    And similar patterns with &lt;
    """
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        
        if in_code_block:
            fixed_lines.append(line)
            continue
        
        # Fix patterns like: "&gt; -> ">
        line = line.replace('"&gt;', '">')
        line = line.replace("'&gt;", "'>")
        line = line.replace('"&lt;', '"<')
        line = line.replace("'&lt;", "'<")
        
        # Also fix if there's still plain &gt; or &lt; in HTML context
        # Pattern: anywhere in an HTML tag
        if '<' in line and '>' in line:
            # Replace &gt; and &lt; that appear between < and >
            # This is a simple approach - replace all in lines with HTML tags
            line = re.sub(r'(<[^>]*?)&gt;([^<]*?>)', r'\1>\2', line)
            line = re.sub(r'(<[^>]*?)&lt;([^<]*?>)', r'\1<\2', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_all_files(docs_dir="docs"):
    """Fix all markdown files."""
    print("=" * 70)
    print("Fixing remaining HTML issues")
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
                content = fix_remaining_html_issues(content)
                
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
    fix_all_files()