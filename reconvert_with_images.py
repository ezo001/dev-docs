import os
import subprocess
import re
from docx import Document

def extract_images_from_docx(docx_path, output_dir):
    """Extract all images from a Word document."""
    doc = Document(docx_path)
    os.makedirs(output_dir, exist_ok=True)
    
    image_count = 0
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image_count += 1
            image_data = rel.target_part.blob
            ext = rel.target_ref.split('.')[-1]
            image_path = os.path.join(output_dir, f"image{image_count}.{ext}")
            with open(image_path, 'wb') as f:
                f.write(image_data)
    
    return image_count

def convert_docx_to_md_with_images(docx_path, md_path, doc_name):
    """Convert DOCX to Markdown using Pandoc with image extraction."""
    
    # Extract images first
    images_dir = f"static/img/docs/{doc_name}"
    extract_images_from_docx(docx_path, images_dir)
    
    # Convert with Pandoc - extract media to the static folder
    cmd = [
        'pandoc',
        docx_path,
        '-f', 'docx',
        '-t', 'markdown',
        '--extract-media', f'static/img/docs/{doc_name}',
        '-o', md_path
    ]
    
    subprocess.run(cmd, check=True)
    
    # Read the generated markdown
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix image paths - Pandoc creates them as media/image.png
    # We need to change them to /img/docs/{doc_name}/media/image.png
    content = re.sub(
        r'!\[(.*?)\]\((media/[^)]+)\)',
        rf'![\1](/img/docs/{doc_name}/\2)',
        content
    )
    
    # Add frontmatter
    title = doc_name.replace('_', ' ').replace('-', ' ').title()
    frontmatter = f"""---
sidebar_position: 1
title: {title}
---

"""
    
    content = frontmatter + content
    
    # Write back
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(content)

def reconvert_all_with_images():
    """Reconvert all Word documents to Markdown with images."""
    
    word_dir = "word-backup"
    docs_dir = "docs"
    
    print("=" * 70)
    print("Converting Word documents to Markdown WITH IMAGES")
    print("=" * 70)
    
    converted = 0
    
    for filename in os.listdir(word_dir):
        if filename.endswith('.docx') and not filename.startswith('~'):
            docx_path = os.path.join(word_dir, filename)
            doc_name = filename.replace('.docx', '')
            md_filename = doc_name + '.md'
            md_path = os.path.join(docs_dir, md_filename)
            
            print(f"\nProcessing: {filename}")
            
            try:
                convert_docx_to_md_with_images(docx_path, md_path, doc_name)
                print(f"  ✓ Converted to {md_filename}")
                converted += 1
            except Exception as e:
                print(f"  ✗ Error: {e}")
    
    print("\n" + "=" * 70)
    print(f"Successfully converted {converted} documents with images!")
    print("=" * 70)
    print("\nNext steps:")
    print("1. Run: npm run build")
    print("2. If successful, commit and push:")
    print("   git add .")
    print('   git commit -m "Restore images in documentation"')
    print("   git push")

if __name__ == "__main__":
    reconvert_all_with_images()