#!/usr/bin/env python3
"""
List which pages contain EMF images in a DOCX (by paragraph index).
Run: python scripts/list_emf_pages.py path/to/file.docx

Page numbers are estimated from paragraph count (approx 30 paras per page);
for exact page numbers use the Word macro. This script confirms EMF presence
and approximate location when the macro cannot run (e.g. TAP blocks extraction).
"""
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

NS_RELS = "{http://schemas.openxmlformats.org/package/2006/relationships}"
NS_W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
NS_A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python list_emf_pages.py <path/to/document.docx>")
        sys.exit(1)
    docx_path = Path(sys.argv[1])
    if not docx_path.exists():
        print("File not found:", docx_path)
        sys.exit(1)

    with zipfile.ZipFile(docx_path, "r") as z:
        # EMF relationship IDs from word/_rels/document.xml.rels
        rels_path = "word/_rels/document.xml.rels"
        if rels_path not in z.namelist():
            print("No document.xml.rels in DOCX")
            sys.exit(1)
        root_rels = ET.fromstring(z.read(rels_path))
        emf_ids = set()
        for rel in root_rels.findall(f".//{NS_RELS}Relationship"):
            target = rel.get("Target") or ""
            if ".emf" in target.lower():
                emf_ids.add(rel.get("Id"))

        if not emf_ids:
            print("No EMF images in this document.")
            sys.exit(0)

        # Paragraph indices that reference EMF blips (from word/document.xml)
        doc_path = "word/document.xml"
        root_doc = ET.fromstring(z.read(doc_path))
        para_indices = []
        idx = 0
        for p in root_doc.iter(NS_W + "p"):
            idx += 1
            for blip in p.iter(NS_A + "blip"):
                embed = blip.get(
                    "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed"
                ) or blip.get("embed")
                if embed in emf_ids:
                    para_indices.append(idx)
                    break

    # Rough page estimate (~30 paragraphs per page)
    paras_per_page = 30
    pages = sorted(set((i - 1) // paras_per_page + 1 for i in para_indices))
    print(f"EMF images: {len(emf_ids)} relationship(s), {len(para_indices)} reference(s) in body.")
    print(f"Paragraph indices (1-based): {para_indices[:20]}{'...' if len(para_indices) > 20 else ''}")
    print(f"Estimated page(s) containing EMF (≈{paras_per_page} paras/page): {pages}")
    print("\nFor exact page numbers, use the Word macro FindEMFImagesInDocument when the document is open.")


if __name__ == "__main__":
    main()
