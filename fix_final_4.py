import os

def fix_specific_lines():
    """Fix the exact problematic lines in the 4 remaining files."""
    
    fixes = {
        "docs/AOT_Azure_Deployment_Guide_Auriga.md": {
            237: lambda line: line.replace('\\<', '<').replace('\\>', '>')
        },
        "docs/AOT_CDF_Deployment_Guide_Auriga.md": {
            297: lambda line: line.replace('\\<', '<').replace('\\>', '>')
        },
        "docs/AOT_Micro_Front_End_MFE_Development_Guide_Auriga.md": {
            539: lambda line: '`' + line.strip() + '`\n'  # Wrap entire line in backticks
        },
        "docs/AOT_Units_of_Measurement_Technical_Reference_Auriga.md": {
            456: lambda line: line.replace(''', "'").replace(''', "'")
        }
    }
    
    print("=" * 70)
    print("Fixing the final 4 files with surgical precision")
    print("=" * 70)
    
    for filepath, line_fixes in fixes.items():
        if not os.path.exists(filepath):
            print(f"Skipping: {filepath} (not found)")
            continue
        
        print(f"Processing: {os.path.basename(filepath)}...")
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            for line_num, fix_func in line_fixes.items():
                if line_num <= len(lines):
                    print(f"  Fixing line {line_num}")
                    lines[line_num - 1] = fix_func(lines[line_num - 1])
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            
            print(f"  ✓ Fixed")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print("=" * 70)
    print("All 4 files processed!")
    print("=" * 70)

if __name__ == "__main__":
    fix_specific_lines()