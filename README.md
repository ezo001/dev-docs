# Technical writing portfolio

A lightweight, static portfolio site — no build step required. Open `index.html` in a browser or deploy to any static host.

## What's included

| Path | Purpose |
|------|---------|
| `index.html` | Landing page: about, work samples, process, skills, contact |
| `samples/*.html` | Four case studies based on common enterprise doc work (sanitized) |
| `css/styles.css` | Typography and layout (Source Serif + Source Sans) |
| `templates/` | Markdown templates for new case studies and resume bullets |

## Quick start

1. **Personalize** `index.html`:
   - Replace `Edward Olson` with your name (all pages)
   - Update email, LinkedIn, and GitHub in the Contact section
   - Adjust the About and hero copy to match your experience

2. **Review case studies** in `samples/`:
   - Content is intentionally generic/sanitized — edit outcomes and details to match what you can claim publicly
   - Add or remove cards on the home page to match your samples

3. **Preview locally:**

   ```bash
   # From the portfolio folder (Python)
   python -m http.server 8080
   # Open http://localhost:8080
   ```

   Or use VS Code **Live Server** / open `index.html` directly.

## Deploy options

### GitHub Pages

1. Create a repo (e.g. `tech-writing-portfolio`).
2. Copy the `portfolio/` folder contents to the repo root (or publish from a `/docs` folder).
3. Settings → Pages → Deploy from branch `main`, folder `/` (or `/docs`).
4. Site URL: `https://<username>.github.io/<repo>/`

### Azure Static Web Apps / Netlify / Cloudflare Pages

- Upload the `portfolio` folder as a static site (no build command).
- Set `index.html` as the default document.

### PDF export (for recruiters)

- Open any sample page in Chrome → Print → Save as PDF.
- `@media print` rules hide nav and footer for cleaner output.

## Adding a new sample

1. Copy `templates/case-study-template.md` and fill it in.
2. Create `samples/your-sample.html` by copying an existing sample page.
3. Add a card to the `#work` section in `index.html`.

## Portfolio checklist (what hiring managers look for)

- [ ] **3–5 case studies** with problem → role → approach → outcomes
- [ ] **At least one writing excerpt** (sanitized if from employer work)
- [ ] **Range of doc types**: tutorial, reference, runbook, or process doc
- [ ] **Tools listed honestly** (Git, static site generators, CCMS, etc.)
- [ ] **Contact + LinkedIn** on every page
- [ ] **No confidential data** — client names, internal URLs, secrets redacted

## Optional next steps

- Add a `resume.pdf` link in the hero or contact section
- Record a 2-minute Loom walking through one case study
- Mirror case studies on LinkedIn Featured section with links back to this site
- Convert to Docusaurus or Astro if you want a blog later (this repo already uses Docusaurus for DevDocs)

## Relationship to DevDocs

This `portfolio/` folder is **separate** from the main Docusaurus site (`docs/`, `MD/`, etc.). Keep employer/internal content out of the public portfolio; use case study format with sanitized excerpts instead.
