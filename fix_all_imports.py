import os

filepath = "docs/AOT_Micro_Front_End_MFE_Development_Guide_Auriga.md"

print("=" * 70)
print("Finding and fixing ALL import/export statements")
print("=" * 70)

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find all lines with import or export
problem_lines = []
in_code_block = False

for i, line in enumerate(lines):
    if line.strip().startswith('```'):
        in_code_block = not in_code_block
        continue
    
    if not in_code_block:
        # Check if line contains import or export keywords
        if 'import ' in line.lower() or 'export ' in line.lower():
            problem_lines.append(i + 1)
            print(f"Line {i+1}: {line.strip()[:80]}...")

print(f"\nFound {len(problem_lines)} problematic lines")
print("=" * 70)

# Fix: Wrap each problematic line in HTML comment
for i in problem_lines:
    idx = i - 1
    if not lines[idx].strip().startswith('<!--'):
        lines[idx] = '<!-- REMOVED: ' + lines[idx].strip() + ' -->\n'
        print(f"Commented out line {i}")

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(lines)

print("=" * 70)
print("✓ All import/export statements commented out")
print("=" * 70)