import os

def strip_all_problematic_chars(filepath):
    """Remove ALL backslashes and replace angle brackets outside code blocks."""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
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
        
        # Remove ALL backslashes
        line = line.replace('\\', '')
        
        # Replace angle brackets with HTML entities
        line = line.replace('<', '&lt;')
        line = line.replace('>', '&gt;')
        
        # Replace smart quotes with regular quotes
        line = line.replace(''', "'")
        line = line.replace(''', "'")
        line = line.replace('"', '"')
        line = line.replace('"', '"')
        
        # Replace curly braces with HTML entities
        line = line.replace('{', '&#123;')
        line = line.replace('}', '&#125;')
        
        fixed_lines.append(line)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)

def fix_final_4():
    """Fix the 4 remaining problematic files."""
    
    files = [
        "docs/AOT_Azure_Deployment_Guide_Auriga.md",
        "docs/AOT_CDF_Deployment_Guide_Auriga.md",
        "docs/AOT_Micro_Front_End_MFE_Development_Guide_Auriga.md",
        "docs/AOT_Units_of_Measurement_Technical_Reference_Auriga.md"
    ]
    
    print("=" * 70)
    print("Nuclear option for final 4 files: HTML entities for everything")
    print("=" * 70)
    
    for filepath in files:
        if not os.path.exists(filepath):
            print(f"Skipping: {filepath} (not found)")
            continue
        
        print(f"Processing: {os.path.basename(filepath)}...", end=" ")
        
        try:
            strip_all_problematic_chars(filepath)
            print("✓ Fixed")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    print("=" * 70)
    print("All 4 files processed!")
    print("=" * 70)

if __name__ == "__main__":
    fix_final_4()