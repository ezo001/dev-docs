# Word to MDX pre-conversion checklist

Use this checklist **before** running the DOCX-to-markdown conversion script. It helps authors (SMEs) and the Doc Team avoid content that breaks MDX or produces poor markdown. For full detail and workflow, see **DOCX-TO-WEB-JOB-AID.md**.

---

## 1. Run Doc Team tools (if available)

- [ ] **MDX Compatibility Validator** — Run on the Word document; fix or note any reported issues.
- [ ] **Auto-correction macros** — Run macros for: quotes, dashes, non-breaking spaces (NBSP), zero-width characters. Re-save the .docx.

---

## 2. Tables

- [ ] **No merged or nested table cells** — Use simple tables: one header row, one row per record.
- [ ] **No multi-line table cells** — Keep each cell on one line; avoid line breaks inside cells (or rewrite so the converter can build a valid pipe table).

---

## 3. Characters and formatting

- [ ] **No smart (curly) quotes** in body text — Use straight quotes (or run the quote macro).
- [ ] **No curly braces in narrative text** — MDX treats braces as code; use words or move code into a code block.
- [ ] **No angle-bracketed URLs or emails** in running text — Use plain URLs or Word Insert Link so the link is stored without angle brackets in the visible text.
- [ ] **No non-breaking spaces (NBSP)** where a normal space is intended — Use the cleanup macro or Find/Replace.

---

## 4. Structure

- [ ] **No blockquotes directly after list items** without a normal paragraph in between — Can cause invalid MDX nesting; add a line of text between the list and the blockquote or avoid the blockquote there.
- [ ] **Code / JSON** — In Word, use a single column or code style; keep snippets on one line where possible. Plan to review the generated code blocks in the .md after conversion.

---

## 5. After conversion (quick check)

- [ ] Run the conversion script (see job aid).
- [ ] Open the generated .md in the repo; spot-check the top (title block, first heading) and any tables or code.
- [ ] Run `npm run build`; fix any reported MDX or build errors.

---

**Doc Team contact:** For questions about the validator, macros, or this checklist, see **CONTRIBUTORS.md** or your Doc Team point of contact.
