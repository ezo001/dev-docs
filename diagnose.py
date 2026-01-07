import os

# Pick one of the failing files
file_path = "docs/AOT_AWS_CDF_Architecture_Auriga.md"

print(f"Reading: {file_path}")
print("=" * 70)

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Show line 373 (where the error is)
print(f"Line 373 (error location):")
print(lines[372] if len(lines) > 372 else "Line not found")
print()

# Show a few lines around it for context
print("Context (lines 370-375):")
for i in range(369, min(375, len(lines))):
    print(f"{i+1}: {lines[i]}", end="")

print("\n" + "=" * 70)
print("\nSearching for ampersands in the file...")
amp_count = 0
for i, line in enumerate(lines, 1):
    if '&' in line and not line.strip().startswith('```'):
        amp_count += 1
        if amp_count <= 5:  # Show first 5 instances
            print(f"Line {i}: {line.strip()[:100]}")

print(f"\nTotal lines with & outside code blocks: {amp_count}")