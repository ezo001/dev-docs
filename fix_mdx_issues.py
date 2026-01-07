import os
import re
import sys

def fix_mdx_issues(file_path):
    """
    Fix all MDX compatibility issues in a markdown file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix 1: Escape ampersands that aren't already HTML entities
        # Replace & with &amp; EXCEPT when it's already part of an HTML entity like &lt; &gt; &amp;
        content = re.sub(r'&(?!(?:lt|gt|amp|nbsp|quot|#\d+|#x[0-9a-fA-F]+);)', '&amp;', content)
        
        # Fix 2: Wrap email addresses in backticks
        email_pattern = r'(?<!`)\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b(?!`)'
        content = re.sub(email_pattern, r'`\1`', content)
        
        # Fix 3: Fix standalone angle brackets (not in HTML tags or code)
        # This is more conservative - only fix obvious cases
        lines = content.split('\n')
        fixed_lines = []
        in_code_block = False
        
        for line in lines:
            # Track code blocks
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                fixed_lines.append(line)
                continue
            
            # Skip lines in code blocks
            if in_code_block:
                fixed_lines.append(line)
                continue
            
            # Fix angle brackets in regular text
            # Only fix < and > that are clearly not HTML tags
            # Escape < that's not followed by a letter (not a tag start)
            line = re.sub(r'<(?![a-zA-Z/])', '&lt;', line)
            # Escape > that's not preceded by a letter or / (not a tag end)
            line = re.sub(r'(?<![a-zA-Z/])>', '&gt;', line)
            
            fixed_lines.append(line)
        
        content = '\n'.join(fixed_lines)
        
        # Fix 4: Escape curly braces in text (but not in code blocks)
        lines = content.split('\n')
        fixed_lines = []
        in_code_block = False
        
        for line in lines:
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                fixed_lines.append(line)
                continue
            
            if not in_code_block and not line.strip().startswith('    '):
                # Wrap standalone curly braces in backticks
                line = re.sub(r'(?<!`)\{([^}]+)\}(?!`)', r'`{\1}`', line)
            
            fixed_lines.append(line)
        
        content = '\n'.join(fixed_lines)
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"  ✗ Error processing {file_path}: {e}")
        return False

def process_directory(docs_dir):
    """
    Process all markdown files in a directory.
    """
    if not os.path.exists(docs_dir):
        print(f"Error: Directory '{docs_dir}' not found!")
        return
    
    print(f"Fixing MDX issues in: {docs_dir}")
    print("-" * 70)
    
    fixed_count = 0
    total_count = 0
    
    for filename in os.listdir(docs_dir):
        if filename.endswith('.md'):
            total_count += 1
            file_path = os.path.join(docs_dir, filename)
            print(f"Processing: {filename}...", end=" ")
            
            if fix_mdx_issues(file_path):
                print("✓ Fixed")
                fixed_count += 1
            else:
                print("○ No changes")
    
    print("-" * 70)
    print(f"Summary: Fixed {fixed_count} out of {total_count} files")
    print("\nNow try running: npm start")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        docs_directory = sys.argv[1]
    else:
        docs_directory = "docs"
    
    process_directory(docs_directory)