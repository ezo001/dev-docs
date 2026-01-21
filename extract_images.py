import os
from docx import Document
import shutil

def extract_images_from_docx(docx_path, output_dir):
    """Extract all images from a Word document."""
    doc = Document(docx_path)
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract images from document relationships
    image_count = 0
    for rel in doc.part.rels.values():
        if "image" in rel.target_ref:
            image_count += 1
            # Get image data
            image_data = rel.target_part.blob
            # Get extension
            ext = rel.target_ref.split('.')[-1]
            # Save image
            image_path = os.path.join(output_dir, f"image{image_count}.{ext}")
            with open(image_path, 'wb') as f:
                f.write(image_data)
    
    return image_count

def extract_all_images():
    """Extract images from all Word documents."""
    word_dir = "word-backup"
    images_dir = "static/img/docs"
    
    print("=" * 70)
    print("Extracting images from Word documents")
    print("=" * 70)
    
    total_images = 0
    results = []
    
    for filename in os.listdir(word_dir):
        if filename.endswith('.docx') and not filename.startswith('~'):
            docx_path = os.path.join(word_dir, filename)
            doc_name = filename.replace('.docx', '')
            output_dir = os.path.join(images_dir, doc_name)
            
            try:
                count = extract_images_from_docx(docx_path, output_dir)
                total_images += count
                results.append(f"{doc_name}: {count} images")
                print(f"✓ {filename}: {count} images")
            except Exception as e:
                print(f"✗ {filename}: Error - {e}")
    
    print("=" * 70)
    print(f"Total: {total_images} images extracted")
    print("=" * 70)
    
    return results

if __name__ == "__main__":
    extract_all_images()