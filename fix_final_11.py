import os
import re

def fix_specific_files(docs_dir="docs"):
    """Fix the 11 remaining problematic files."""
    
    problem_files = [
        "AOT_Azure_Deployment_Guide_Auriga.md",
        "AOT_Azure_Smart_KPIs_API_Reference_Auriga.md",
        "AOT_CDF_Deployment_Guide_Auriga.md",
        "AOT_KPI_Hierarchy_and_Calculation_Technical_Overview_Auriga.md",
        "AOT_Micro_Front_End_MFE_Development_Guide_Auriga.md",
        "AOT_Operations_Hierarchy_API_Reference_Auriga.md",
        "AOT_Reports_Delivery_Guide_Auriga.md",
        "AOT_Smart_KPIs_API_Reference_Auriga.md",
        "AOT_Twin_Viewer_Builder_API_Reference_Auriga.md",
        "AOT_Units_of_Measurement_Technical_Reference_Auriga.md"
    ]
    
    print("=" * 70)
    print("Fixing the final 11 problematic files")
    print("=" * 70)
    
    for filename in problem_files:
        filepath = os.path.join(docs_dir, filename)
        if not os.path.exists(filepath):
            print(f"Skipping: {filename} (not found)")
            continue
            
        print(f"Processing: {filename}...", end=" ")
        
        try:
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
                
                # Aggressively escape ALL curly braces outside code blocks
                line = line.replace('{', '\\{')
                line = line.replace('}', '\\}')
                
                # Also fix any stray backtick-angle bracket combos
                line = line.replace('`\\<`', '\\<')
                line = line.replace('`\\>`', '\\>')
                
                fixed_lines.append(line)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(fixed_lines)
            
            print("✓ Fixed")
            
        except Exception as e:
            print(f"✗ Error: {e}")
    
    print("=" * 70)
    print("All 11 files processed")
    print("=" * 70)

if __name__ == "__main__":
    fix_specific_files()