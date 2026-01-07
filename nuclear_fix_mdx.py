import os
import re
import sys

def fix_ampersands_everywhere(content):
    """
    Nuclear option: Replace ALL ampersands with &amp; except those already in HTML entities.
    This catches ampersands in URLs, attributes, text - everywhere.
    """
    # First pass: mark already-valid HTML entities so we don't break them
    # Temporarily replace valid entities with placeholders
    entity_pattern = r'&(lt|gt|amp|nbsp|quot|apos|#\d+|#x[0-9a-fA-F]+);'
    entities_found = []
    
    def save_entity(match):
        entities_found.append(match.group(0))
        return f"__ENTITY_{len(entities_found)-1}__"
    
    content = re.sub(entity_pattern, save_entity, content)
    
    # Second pass: replace ALL remaining ampersands
    content = content.replace('&', '&amp;')
    
    # Third pass: restore the saved entities
    for i, entity in enumerate(entities_found):
        content = content.replace(f"__ENTITY_{i}__", entity)
    
    return content

def fix_curly_braces_in_text(content):
    """
    Escape curly braces that MDX might interpret as JSX expressions.
    """
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        
        if not in_code_block:
            # Escape curly braces in non-code content
            # Only if they're not already in backticks
            if '{' in line or '}' in line:
                # Simple approach: wrap any { } pair in backticks
                line = re.sub(r'(?<!`)\{([^}]{1,100})\}(?!`)', r'`{\1}`', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_mdx_file(file_path):
    """
    Fix all MDX compatibility issues in a single file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes in order
        # 1. Fix ALL ampersands (this is the main issue)
        content = fix_ampersands_everywhere(content)
        
        # 2. Fix curly braces
        content = fix_curly_braces_in_text(content)
        
        # 3. Fix email addresses (wrap in backticks)
        email_pattern = r'(?<!`)\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b(?!`)'
        content = re.sub(email_pattern, r'`\1`', content)
        
        # Only write if changes were made
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False

def process_directory(docs_dir):
    """
    Process all markdown files in the docs directory.
    """
    if not os.path.exists(docs_dir):
        print(f"Error: Directory '{docs_dir}' not found!")
        return
    
    print("=" * 70)
    print(f"NUCLEAR OPTION: Fixing ALL ampersands in: {docs_dir}")
    print("=" * 70)
    
    fixed_count = 0
    total_count = 0
    
    for filename in os.listdir(docs_dir):
        if filename.endswith('.md'):
            total_count += 1
            file_path = os.path.join(docs_dir, filename)
            print(f"Processing: {filename}...", end=" ")
            
            if fix_mdx_file(file_path):
                print("✓ Fixed")
                fixed_count += 1
            else:
                print("○ No changes")
    
    print("=" * 70)
    print(f"Fixed {fixed_count} out of {total_count} files")
    print("=" * 70)
    print("\nNow try: npm start")

if __name__ == "__main__":
    docs_directory = sys.argv[1] if len(sys.argv) > 1 else "docs"
    process_directory(docs_directory)