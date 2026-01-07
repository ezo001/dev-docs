import os
import re

def fix_malformed_html_and_ampersands(content):
    """
    Fix multiple issues:
    1. Malformed HTML like: ";&gt; or ";&lt; 
    2. &lt and &gt that should be angle brackets
    3. Any remaining bare ampersands
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
        
        # Skip code blocks
        if in_code_block:
            fixed_lines.append(line)
            continue
        
        # Fix 1: Malformed HTML like: ";&gt; should be ">
        line = re.sub(r'";(&gt;|&lt;)', r'">', line)
        line = re.sub(r"';(&gt;|&lt;)", r"'>", line)
        
        # Fix 2: &lt`email`&gt; patterns should be `<email>`
        line = re.sub(r'&lt;?`([^`]+)`&gt;?', r'`<\1>`', line)
        
        # Fix 3: Convert remaining &lt; and &gt; back to < and >
        # BUT be careful - some might be legitimate
        # Only convert if they're not part of valid HTML entities
        
        # Fix 4: Replace ALL remaining bare ampersands with &amp;
        # First, save existing valid entities
        entity_pattern = r'&(lt|gt|amp|nbsp|quot|apos|#\d+|#x[0-9a-fA-F]+);'
        entities_found = []
        
        def save_entity(match):
            entities_found.append(match.group(0))
            return f"__ENTITY_{len(entities_found)-1}__"
        
        line = re.sub(entity_pattern, save_entity, line)
        
        # Now replace all remaining ampersands
        line = line.replace('&', '&amp;')
        
        # Restore saved entities
        for i, entity in enumerate(entities_found):
            line = line.replace(f"__ENTITY_{i}__", entity)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_file(filepath):
    """Fix a single markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        content = fix_malformed_html_and_ampersands(content)
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def process_all_docs(docs_dir="docs"):
    """Process all markdown files."""
    print("=" * 70)
    print("Fixing malformed HTML and ampersands")
    print("=" * 70)
    
    fixed_count = 0
    total_count = 0
    
    for filename in os.listdir(docs_dir):
        if filename.endswith('.md'):
            total_count += 1
            filepath = os.path.join(docs_dir, filename)
            print(f"Processing: {filename}...", end=" ")
            
            if fix_file(filepath):
                print("✓ Fixed")
                fixed_count += 1
            else:
                print("○ No changes")
    
    print("=" * 70)
    print(f"Fixed {fixed_count} out of {total_count} files")
    print("=" * 70)

if __name__ == "__main__":
    process_all_docs()