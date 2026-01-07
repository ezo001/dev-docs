import os
import re

def fix_all_mdx_issues(content):
    """
    Fix remaining MDX issues:
    1. Unclosed HTML tags
    2. Curly braces outside code blocks
    3. Backslashes in HTML
    4. Unexpected slashes in HTML
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
        
        # Fix 1: Remove stray HTML tags that are unclosed
        # These are causing "Expected closing tag" errors
        # Simple approach: if a line has <td> or <th> or <li> without matching </...>, wrap in backticks
        if ('<td' in line or '<th' in line or '<li' in line or '<tr' in line):
            # Count opening and closing tags
            opens = len(re.findall(r'<(td|th|li|tr)[\s>]', line))
            closes = len(re.findall(r'</(td|th|li|tr)>', line))
            
            # If mismatched, the HTML is malformed - escape it
            if opens != closes:
                # Wrap entire line content in backticks if it contains HTML
                line = '`' + line.strip() + '`'
        
        # Fix 2: Wrap curly braces in backticks (causes acorn errors)
        # But NOT if they're already in backticks
        if '{' in line or '}' in line:
            # Only fix if not already in backticks and not in a code fence
            if '`' not in line or line.count('{') > line.count('`{'):
                line = re.sub(r'(?<!`)\{([^}]{1,100})\}(?!`)', r'`{\1}`', line)
        
        # Fix 3: Remove backslashes from HTML-like content
        if '\\' in line and ('<' in line or '>' in line):
            line = line.replace('\\', '')
        
        # Fix 4: Unexpected `/` - usually in malformed HTML like </something> without proper opening
        # Escape lines with stray closing tags
        if re.search(r'<\s*/\s*[^>]+>', line) and not re.search(r'<[^/][^>]*>.*</[^>]+>', line):
            line = '`' + line.strip() + '`'
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def process_all_files(docs_dir="docs"):
    """Process all markdown files."""
    print("=" * 70)
    print("Fixing remaining MDX issues (HTML tags, curly braces, etc.)")
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
                content = fix_all_mdx_issues(content)
                
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
    print("\nFor the 2 missing image files, you can either:")
    print("1. Add the image files to a 'media' folder in docs/")
    print("2. Or remove those image references from the markdown files")

if __name__ == "__main__":
    process_all_files()