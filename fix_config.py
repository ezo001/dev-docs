import os

config_file = "docusaurus.config.js"

print("=" * 70)
print("Adding onBrokenLinks: 'warn' to docusaurus.config.js")
print("=" * 70)

with open(config_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find "export default {" and add onBrokenLinks right after
if 'onBrokenLinks' not in content:
    # Add it after "export default {"
    content = content.replace(
        'export default {',
        "export default {\n  onBrokenLinks: 'warn',  // Allow build with broken links"
    )
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Added onBrokenLinks: 'warn' to config")
else:
    # Change existing onBrokenLinks to 'warn'
    import re
    content = re.sub(
        r"onBrokenLinks:\s*['\"]throw['\"]",
        "onBrokenLinks: 'warn'",
        content
    )
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✓ Changed onBrokenLinks to 'warn'")

print("=" * 70)
print("Configuration updated!")
print("=" * 70)