import os

filepath = "docs/AOT_Micro_Front_End_MFE_Development_Guide_Auriga.md"

print("=" * 70)
print("Inspecting line 541 of MFE Development Guide")
print("=" * 70)

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show lines around 541
print(f"\nLines 535-545:")
for i in range(534, min(545, len(lines))):
    print(f"{i+1}: {lines[i]}", end="")

print("\n" + "=" * 70)
print("Fixing by wrapping problematic lines in code fence")
print("=" * 70)

# Wrap lines 535-545 in a code block if they're not already
in_code_block = False
for i in range(len(lines)):
    if lines[i].strip().startswith('```'):
        in_code_block = not in_code_block

# Check if line 541 is in a code block
in_code_block = False
for i in range(540):
    if lines[i].strip().startswith('```'):
        in_code_block = not in_code_block

if not in_code_block:
    print("Line 541 is NOT in a code block. Wrapping it...")
    # Find the problematic section and wrap it
    # Insert ``` before line 540 and after line 545
    lines.insert(539, '```\n')
    lines.insert(546, '```\n')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("✓ Wrapped lines 540-545 in code fence")
else:
    print("Line 541 is already in a code block. Trying different approach...")
    # Just comment out or delete line 541
    lines[540] = '<!-- ' + lines[540].rstrip() + ' -->\n'
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print("✓ Commented out line 541")

print("=" * 70)