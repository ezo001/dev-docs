import os
import re
import sys

def fix_ampersands_smart(content):
    """
    Replace ALL ampersands with &amp; EXCEPT:
    1. Those already in HTML entities
    2. Those inside code blocks (```...```)
    3. Those inside inline code (`...`)
    """
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    
    for line in lines:
        # Check if we're entering/exiting a code block
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        
        # If we're in a code block, don't touch it
        if in_code_block:
            fixed_lines.append(line)
            continue
        
        # If we're NOT in a code block, process the line
        # But we need to protect inline code (`...`)
        
        # Split line by inline code blocks
        parts = []
        last_end = 0
        
        # Find all inline code blocks
        for match in re.finditer(r'`[^`]+`', line):
            # Add text before the code block (this gets fixed)
            before = line[last_end:match.start()]
            parts.append(('text', before))
            
            # Add the code block (this stays unchanged)
            parts.append(('code', match.group(0)))
            
            last_end = match.end()
        
        # Add any remaining text after the last code block
        if last_end < len(line):
            parts.append(('text', line[last_end:]))
        
        # If no inline code was found, treat the whole line as text
        if not parts:
            parts = [('text', line)]
        
        # Now fix ampersands only in text parts
        fixed_line = ''
        for part_type, part_content in parts:
            if part_type == 'text':
                # Fix ampersands in this text section
                # First, save existing HTML entities
                entity_pattern = r'&(lt|gt|amp|nbsp|quot|apos|#\d+|#x[0-9a-fA-F]+);'
                entities_found = []
                
                def save_entity(match):
                    entities_found.append(match.group(0))
                    return f"__ENTITY_{len(entities_found)-1}__"
                
                part_content = re.sub(entity_pattern, save_entity, part_content)
                
                # Replace all remaining ampersands
                part_content = part_content.replace('&', '&amp;')
                
                # Restore saved entities
                for i, entity in enumerate(entities_found):
                    part_content = part_content.replace(f"__ENTITY_{i}__", entity)
            
            fixed_line += part_content
        
        fixed_lines.append(fixed_line)
    
    return '\n'.join(fixed_lines)

def fix_email_addresses(content):
    """
    Wrap email addresses in backticks (but not if already in code blocks).
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
            # Fix emails not already in backticks
            email_pattern = r'(?<!`)\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b(?!`)'
            line = re.sub(email_pattern, r'`\1`', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_curly_braces(content):
    """
    Escape curly braces outside of code blocks.
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
            # Wrap curly braces in backticks (simple cases only)
            line = re.sub(r'(?<!`)\{([^}`]{1,100})\}(?!`)', r'`{\1}`', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_mdx_file(file_path):
    """
    Fix all MDX compatibility issues while preserving code blocks.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply fixes in order
        # 1. Fix ampersands (but protect code blocks)
        content = fix_ampersands_smart(content)
        
        # 2. Fix email addresses
        content = fix_email_addresses(content)
        
        # 3. Fix curly braces
        content = fix_curly_braces(content)
        
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
    print(f"Smart Fix: Protecting code blocks while fixing ampersands")
    print(f"Processing: {docs_dir}")
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
    print("\n✅ Code blocks and inline code are protected!")
    print("Now try: npm start")

if __name__ == "__main__":
    docs_directory = sys.argv[1] if len(sys.argv) > 1 else "docs"
    process_directory(docs_directory)