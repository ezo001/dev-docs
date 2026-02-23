# Find EMF Images macro (Word)

The macro **FindEMFImagesInDocument** lists the **page numbers** in the active document that contain EMF (Enhanced Metafile) images. Use it to know where to replace EMFs with PNG or other web-friendly formats before or after conversion.

## Install

1. Open **Word**.
2. Press **Alt+F11** to open the VBA editor (or **Developer** tab → **Visual Basic**).
3. **File** → **Import File**.
4. Browse to `scripts/FindEMFImages.bas` and open it.
5. Close the VBA editor.

## Run

1. Open the **.docx** you want to check (the document must be **saved** so the macro can read its package).
2. Press **Alt+F8** (or **Developer** → **Macros**).
3. Select **FindEMFImagesInDocument** → **Run**.

A dialog lists the **page number(s)** that include at least one EMF image.

## What it does

- **Linked EMF pictures**: Detects images whose source path ends with `.emf`.
- **Embedded EMF pictures**: Opens the .docx as a zip, reads `word/_rels/document.xml.rels` and `word/document.xml`, finds relationship IDs for `.emf` parts, then finds which paragraphs reference them and gets their page numbers.

## Requirements

- Word with VBA enabled.
- Document saved as **.docx** (macro will prompt to save if not).
- No extra references needed; uses `MSXML2.DOMDocument.6.0` and `Shell.Application` (standard on Windows).
- The macro does **not** run cmd.exe, tar, or PowerShell, so it works when IT policy (e.g. Trusted Application Protection / TAP) blocks those.
