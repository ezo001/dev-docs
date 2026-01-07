import os

file_path = "docs/AOT_AWS_CDF_Architecture_Auriga.md"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Line 373 NOW:")
print(lines[372])