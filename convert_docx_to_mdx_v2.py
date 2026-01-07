import os
import re
import subprocess
import sys
from pathlib import Path

def convert_docx_to_markdown(docx_path, output_path):
    """
    Convert a Word document to markdown using Pandoc.
    Returns True if successful, False otherwise.
    """
    try:
        # Use Pandoc to convert docx to markdown
        # --wrap=none prevents hard line wrapping
        # -f docx specifies input format
        # -t gfm specifies GitHub Flavored Markdown output
        result = subprocess.run(
            ['pandoc', '-f', 'docx', '-t', 'gfm', '--wrap=none', docx_path, '-o', output_path],
            capture_output=True,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ✗ Pandoc conversion failed: {e.stderr}")
        return False
    except FileNotFoundError:
        print("  ✗ Error: Pandoc is not installed or not in PATH")
        print("  Install Pandoc from: https://pandoc.org/installing.html")
        return False

def create_docusaurus_frontmatter(title):
    """
    Create Docusaurus frontmatter for the markdown file.
    """
    # Clean up title - remove file extension and special chars
    clean_title = title.replace('.md', '').replace('_', ' ')
    # Create a URL-safe ID
    doc_id = title.replace('.md', '').lower().replace(' ', '-').replace('_', '-')
    
    frontmatter = f"""---
id: {doc_id}
title: {clean_title}
---

"""
    return frontmatter

def fix_ampersands(content):
    """
    Fix ampersands - this is the most critical fix for MDX.
    Replace & with &amp; EXCEPT when it's already part of an HTML entity.
    """
    # Replace & with &amp; EXCEPT when followed by known HTML entities
    content = re.sub(r'&(?!(?:lt|gt|amp|nbsp|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', content)
    return content

def fix_email_addresses(content):
    """
    Wrap email addresses in backticks to prevent MDX from parsing @ as JSX.
    """
    # Pattern to match email addresses that are NOT already in backticks
    email_pattern = r'(?<!`)\b([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\b(?!`)'
    content = re.sub(email_pattern, r'`\1`', content)
    return content

def fix_angle_brackets(content):
    """
    Fix standalone angle brackets that MDX might interpret as JSX tags.
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
        
        # Skip lines in code blocks
        if in_code_block:
            fixed_lines.append(line)
            continue
        
        # Fix angle brackets in regular text
        # Escape < that's not followed by a letter (not an HTML tag start)
        line = re.sub(r'<(?![a-zA-Z/!])', '&lt;', line)
        # Escape > that's not part of an HTML tag
        line = re.sub(r'(?<![a-zA-Z/\-])>(?!\s*\n)', '&gt;', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_curly_braces(content):
    """
    Wrap curly braces in backticks to prevent MDX from interpreting them as JSX expressions.
    """
    lines = content.split('\n')
    fixed_lines = []
    in_code_block = False
    
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed_lines.append(line)
            continue
        
        if not in_code_block and not line.strip().startswith('    '):
            # Wrap standalone curly braces in backticks (but not if already in backticks)
            # This is conservative - only wraps simple cases
            line = re.sub(r'(?<!`)\{([^}]{1,50})\}(?!`)', r'`{\1}`', line)
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)

def fix_nested_tables(content):
    """
    Remove or simplify overly complex tables that cause MDX issues.
    """
    lines = content.split('\n')
    fixed_lines = []
    in_table = False
    table_buffer = []
    
    for line in lines:
        # Detect table rows
        if '|' in line and not line.strip().startswith('#'):
            in_table = True
            # Check if this line has excessive complexity (likely nested)
            pipe_count = line.count('|')
            if pipe_count > 15:  # Arbitrary threshold for "too complex"
                # Skip overly complex table rows
                continue
            table_buffer.append(line)
        else:
            if in_table and table_buffer:
                # End of table - add buffered lines
                fixed_lines.extend(table_buffer)
                table_buffer = []
                in_table = False
            fixed_lines.append(line)
    
    # Add any remaining table buffer
    if table_buffer:
        fixed_lines.extend(table_buffer)
    
    return '\n'.join(fixed_lines)

def remove_problematic_html(content):
    """
    Remove or fix HTML that causes MDX issues.
    """
    # Remove HTML comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Convert common problematic HTML entities
    html_entities = {
        '&nbsp;': ' ',
        '&mdash;': '—',
        '&ndash;': '–',
        '&ldquo;': '"',
        '&rdquo;': '"',
        '&lsquo;': "'",
        '&rsquo;': "'",
        '&hellip;': '...',
    }
    for entity, replacement in html_entities.items():
        content = content.replace(entity, replacement)
    
    return content

def fix_all_mdx_issues(content, filename):
    """
    Apply all fixes to make markdown MDX-compatible.
    This is applied in a specific order for best results.
    """
    print(f"  → Applying MDX fixes...")
    
    # Order matters! Do these in sequence:
    
    # 1. Remove problematic HTML first
    content = remove_problematic_html(content)
    
    # 2. Fix ampersands (CRITICAL - must be done early)
    content = fix_ampersands(content)
    
    # 3. Fix email addresses
    content = fix_email_addresses(content)
    
    # 4. Fix nested tables
    content = fix_nested_tables(content)
    
    # 5. Fix angle brackets
    content = fix_angle_brackets(content)
    
    # 6. Fix curly braces
    content = fix_curly_braces(content)
    
    # 7. Add Docusaurus frontmatter at the very end
    content = create_docusaurus_frontmatter(filename) + content
    
    return content

def process_docx_file(docx_path, output_dir):
    """
    Convert a single docx file to MDX-compatible markdown.
    """
    filename = os.path.basename(docx_path)
    output_filename = os.path.splitext(filename)[0] + '.md'
    output_path = os.path.join(output_dir, output_filename)
    temp_path = output_path + '.temp'
    
    print(f"\n📄 Processing: {filename}")
    
    # Step 1: Convert with Pandoc
    print(f"  → Converting with Pandoc...")
    if not convert_docx_to_markdown(docx_path, temp_path):
        return False
    
    # Step 2: Read the converted markdown
    try:
        with open(temp_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  ✗ Error reading converted file: {e}")
        return False
    
    # Step 3: Apply all MDX fixes
    content = fix_all_mdx_issues(content, output_filename)
    
    # Step 4: Write the fixed markdown
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        # Remove temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)
        print(f"  ✓ Successfully created: {output_filename}")
        return True
    except Exception as e:
        print(f"  ✗ Error writing output file: {e}")
        return False

def process_directory(docx_dir, output_dir):
    """
    Process all docx files in a directory.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Find all docx files
    docx_files = []
    for ext in ['*.docx', '*.DOCX']:
        docx_files.extend(Path(docx_dir).glob(ext))
    
    # Filter out temporary Word files (starting with ~$)
    docx_files = [f for f in docx_files if not os.path.basename(str(f)).startswith('~$')]
    
    if not docx_files:
        print(f"No .docx files found in: {docx_dir}")
        return
    
    print("=" * 70)
    print(f"Found {len(docx_files)} Word document(s) to convert")
    print(f"Input directory:  {docx_dir}")
    print(f"Output directory: {output_dir}")
    print("=" * 70)
    
    success_count = 0
    fail_count = 0
    
    for docx_file in docx_files:
        if process_docx_file(str(docx_file), output_dir):
            success_count += 1
        else:
            fail_count += 1
    
    print("\n" + "=" * 70)
    print(f"✓ Successfully converted: {success_count}")
    print(f"✗ Failed: {fail_count}")
    print("=" * 70)
    
    if success_count > 0:
        print(f"\n✨ Markdown files are ready in: {output_dir}")
        print("   You can now run: npm start")
        print("\n💡 If you still get errors, run:")
        print(f"   python fix_mdx_issues.py {output_dir}")

def main():
    """
    Main function - handles command line arguments.
    """
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python convert_docx_to_mdx.py <input_directory> [output_directory]")
        print("\nExample:")
        print("  python convert_docx_to_mdx.py ./word_docs ./docs")
        print("  python convert_docx_to_mdx.py docx-for-conversion docs")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "docs"
    
    if not os.path.exists(input_dir):
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)
    
    process_directory(input_dir, output_dir)

if __name__ == "__main__":
    main()