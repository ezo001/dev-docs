import os
import re

def strip_all_html_tables(content):
    """
    Remove ALL HTML table tags and just leave the content as plain text.
    This is a nuclear option but will get the build working.
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
        
        # Remove ALL HTML tags outside code blocks
        # This includes: <table>, <tbody>, <thead>, <tr>, <td>, <th>, <ul>, <li>, etc.
        line = re.sub(r'</?(?:table|tbody|thead|tfoot|tr|td|th|ul|ol|li|colgroup|col)[^>]*>', '', line)
        
        # Also remove any stray closing tags
        line = re.sub(r'</[a-z]+>', '', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def escape_special_chars_for_mdx(content):
    """
    Escape characters that MDX interprets as JSX.
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
        
        # Wrap unmatched curly braces in backticks
        # Count braces
        open_braces = line.count('{')
        close_braces = line.count('}')
        
        if open_braces != close_braces or (open_braces > 0 and '`{' not in line):
            # Escape all curly braces
            line = re.sub(r'(?<!`)\{', r'`{`', line)
            line = re.sub(r'(?<!`)\}', r'`}`', line)
            # Clean up double backticks
            line = line.replace('``', '')
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def process_all_files(docs_dir="docs"):
    """Process all markdown files."""
    print("=" * 70)
    print("NUCLEAR OPTION: Stripping ALL HTML tables")
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
                
                # Step 1: Strip all HTML tables
                content = strip_all_html_tables(content)
                
                # Step 2: Escape special characters
                content = escape_special_chars_for_mdx(content)
                
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
    print("\nNote: All HTML tables have been converted to plain text.")
    print("The tables will need to be manually reformatted as Markdown tables later.")

if __name__ == "__main__":
    process_all_files()