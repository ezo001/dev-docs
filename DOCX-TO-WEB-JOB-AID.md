# Job Aid: SharePoint DOCX → Static Web App (Markdown)

This guide walks you from downloading Word documents from SharePoint through to having them published as markdown on your Azure Static Web App.

**Access:** Only people with an **@accenture.com** email address may access the published documents. The Azure Static Web App (and any auth in front of it) should be configured to enforce this.

---

## Prerequisites

- **Pandoc** installed ([https://pandoc.org/installing.html](https://pandoc.org/installing.html)) — required for conversion
- **Python 3** — to run the conversion script
- **Node.js 20+** — for the Docusaurus site (`npm run build` / `npm start`)
- **Git** — to push changes to the repo that deploys to Azure
- Access to the **SharePoint** library where the .docx files live
- Access to the **GitHub repo** that is connected to your Azure Static Web App

---

## Step 1: Download the DOCX files from SharePoint

1. Open the SharePoint document library that contains the Word documents you want to publish.
2. Select the .docx files you need (use checkboxes or **Select all** if converting the whole set).
3. Use **Download** (or **Copy to** / **Open in OneDrive** then download):
   - If SharePoint offers **Download** for multiple files, you may get a **.zip** file.
   - If you can only download one at a time, download each .docx to the same folder on your PC.
4. If you received a .zip:
   - Move the .zip to a convenient location (e.g. your Desktop or a `downloads` folder).
   - Right‑click the .zip → **Extract All** (Windows) or double‑click to open and drag the contents out (Mac).
   - Note the path to the **folder** that now contains the .docx files (e.g. `C:\Users\YourName\Desktop\SharePoint-Docs`).

**Tip:** Avoid spaces and special characters in the folder name (e.g. `word-docs` or `docx-for-conversion`).

---

## Step 2: Put the DOCX files in a logical folder

Use the **DOCX / MD** layout so you can add or retire assets (Thread, IAI, etc.) without editing config. See **ASSETS-FOLDER-GUIDE.md** for full details. **Note:** AOT docs have been retired; IAI covers that content.

1. Open the folder where your Docusaurus project lives (e.g. `my-docs`).
2. Put source .docx files in **DOCX** under a subfolder for that asset:
   - **Digital Thread** → `DOCX/Thread/`
   - **Industrial AI** → `DOCX/IAI/`
   - **New asset** → create a new subfolder under `DOCX/` (e.g. `DOCX/MyAsset/`) and put .docx there.
3. Put **only** the .docx files you want to convert in that asset folder (no fixed list to maintain).

**Example layout:**

```
my-docs/
├── DOCX/               ← Source Word files (one subfolder per asset)
│   ├── Thread/        ← Digital Thread .docx
│   └── IAI/           ← Industrial AI .docx
├── MD/                 ← Converted markdown (same subfolder names)
│   ├── Thread/
│   └── IAI/
├── convert_docx_to_markdown.py
└── package.json
```

**Note:** The repo and Azure deployment do not store the .docx source files; they remain in SharePoint. Only the converted `MD/` content and `docs/` are in Git (see `.gitignore`: `DOCX/`, `*.docx`). Use `DOCX/` locally only for running the conversion script.

---

## Before converting: Word do's and don'ts

Word formatting often introduces characters or structures that break MDX or produce poor markdown. **Before you run the conversion script**, authors (SMEs) and the Doc Team should prepare the .docx so conversion is reliable.

**Use the Doc Team tools (recommended):**

- **MDX Compatibility Validator** — Run on the Word document to flag issues before conversion.
- **Auto-correction macros** — Fix quotes, dashes, non-breaking spaces (NBSP), and zero-width characters. Run these macros on the .docx before saving and converting.

**In Word, avoid or fix:**

| Avoid | Why | What to do instead |
|-------|-----|--------------------|
| Merged or nested tables | Conversion breaks or produces invalid MDX. | Use simple tables: one header row, one row per record; no merged cells. |
| Multi-line table cells | Breaks pipe-table parsing. | Put each cell on one line; use line breaks sparingly or rewrite. |
| Smart (curly) quotes | Can break MDX strings. | Use the macros to convert to straight quotes, or type straight quotes. |
| Curly braces `{` `}` in body text | MDX treats `{` as code. | Use macros or replace with words (e.g. "set" instead of "{" where appropriate); keep braces only in code blocks. |
| Angle-bracketed URLs or emails (`<url>`) | Treated as HTML/MDX tags. | Use plain URLs or link text; or use the link dialog so Word stores a hyperlink without angle brackets in text. |
| Blockquotes immediately after list items | Can produce invalid nesting. | Add a normal paragraph between the list and the blockquote, or avoid blockquotes there. |
| Non-breaking spaces (NBSP) | Can cause odd spacing or break parsing. | Use the cleanup macro or Find/Replace to normal spaces. |

**For code or JSON:** Put snippets in a single column table or a dedicated "code" style and keep content on one line where possible; the converter may emit code blocks. Do not rely on Word formatting alone for code — review the generated `.md` after conversion.

**Checklist:** Use **WORD-TO-MDX-CHECKLIST.md** in this repo as a quick pre-conversion checklist for authors and the Doc Team.

---

## Step 3: Run the conversion script

1. Open a terminal and go to your project folder:
   ```bash
   cd C:\Users\YourName\Desktop\my-docs
   ```
2. **Option A — Convert all assets** (recommended if using DOCX/MD layout):  
   Converts every subfolder under `DOCX` that contains .docx into the matching subfolder under `MD`. No prompts; no list to maintain.
   ```bash
   python convert_docx_to_markdown.py --all
   ```
3. **Option B — Convert one asset** (or use prompts):  
   ```bash
   python convert_docx_to_markdown.py
   ```
   When prompted:
   - **Enter path to folder containing .docx files:** e.g. `DOCX\IAI` or `DOCX\Thread`.
   - **Enter output folder for .md files [docs]:** e.g. `MD\IAI` or `MD\Thread`.
4. Or run without prompts:
   ```bash
   python convert_docx_to_markdown.py DOCX\IAI MD\IAI
   python convert_docx_to_markdown.py DOCX\Thread MD\Thread
   ```
5. The script will run Pandoc, extract images to `media/`, clean for MDX, and add frontmatter. Check the summary (e.g. “SUCCESS: Converted 5/5 documents”).

**Keep existing .md and only add/update:**

```bash
python convert_docx_to_markdown.py --all --no-clear
```

---

## Step 4: Review the markdown locally (recommended)

1. In the same project folder, start the Docusaurus dev server:
   ```bash
   npm start
   ```
2. Open the URL shown (e.g. [http://localhost:3000](http://localhost:3000)).
3. In the sidebar, open the new docs and check:
   - Titles and headings
   - Tables
   - Images (paths like `media/...`)
   - Links and formatting
4. Fix any issues in the .md files under `docs/` (or your chosen output folder), then run `npm start` again if needed.
5. Stop the dev server when done (Ctrl+C in the terminal).

**Doc page structure (title and H1):** The doc title (e.g. "IAI Architecture Azure") appears only in the **sidebar** and **breadcrumbs**—not as a big heading in the content area. The content area uses the **topic line** in the doc-title-block (e.g. "Azure Deployment", "General Architecture") as the main H1. The conversion script outputs this block; do not add a duplicate `# Doc Title` at the top of the body. This applies to all existing and future converted docs.

---

## Step 5: Build the site to confirm it compiles

1. In the project folder, run:
   ```bash
   npm run build
   ```
2. If the build finishes without errors, the content is ready to deploy.
3. If you see errors (e.g. broken image paths or MDX syntax), fix the reported files and run `npm run build` again.

---

## Step 6: Commit and push to GitHub

1. In your project folder, check what changed:
   ```bash
   git status
   ```
   You should see new or modified files under `docs/` (and possibly `docs/media/`).
2. Stage the doc and image changes:
   ```bash
   git add docs/
   ```
   (If you used a different output folder, add that folder instead.)
3. Commit with a clear message:
   ```bash
   git commit -m "Add/update docs from SharePoint DOCX conversion"
   ```
4. Push to the branch that triggers deployment (usually `main`):
   ```bash
   git push origin main
   ```

**Approval before publish (recommended workflow)**  
To match the desired doc lifecycle (approval routing, then deploy), use a **pull request** instead of pushing straight to `main`:

1. Create a branch, commit your changes, and push the branch:
   ```bash
   git checkout -b docs/update-iai-march
   git add MD/
   git commit -m "Add/update docs from SharePoint DOCX conversion"
   git push origin docs/update-iai-march
   ```
2. In GitHub, open a **Pull request** from `docs/update-iai-march` into `main`. Add a short description (e.g. which docs changed and why).
3. A doc owner or teammate **reviews** the diff (and optionally the built site via a preview). They approve or request changes.
4. When approved, **merge** the PR. Merging to `main` triggers the GitHub Actions workflow; the site builds and deploys. No one merges without review if you use this workflow.

**Release-time review for existing web docs**  
For docs already on the site, do a **release-time review** before or after a release: open the changed or new pages on the live site, spot-check headings, tables, links, and code blocks. Minor fixes can be made via **Edit this page** (and, if you use approval workflow, via a PR). Approved pages are published when the merged PR triggers the deploy.

---

## Step 7: Let Azure Static Web Apps deploy

1. Pushing to `main` triggers the GitHub Actions workflow (e.g. “Azure Static Web Apps CI/CD”).
2. In GitHub, open your repo → **Actions** and watch the latest workflow run. It will:
   - Check out the repo
   - Build the app (output to `build`)
   - Deploy to Azure Static Web Apps
3. Wait until the workflow shows a green checkmark (success).
4. If it fails, open the failed run and read the log (e.g. build errors or missing secrets). Fix the issue, commit, and push again.

---

## Step 8: Confirm docs are live on the static web app

1. In Azure Portal, open your **Static Web App** resource.
2. Copy the **URL** from the overview (e.g. `https://thankful-ground-02a600f10.azurestaticapps.net`).
3. Open that URL in a browser and go to the docs section.
4. Confirm the new or updated pages and images load correctly.

Your SharePoint-sourced content is now published as markdown on the static web app.

---

## Managing your Azure Static Web App

**Deleting extra Static Web Apps** — If you have multiple SWAs (e.g. from testing or old projects), keep the one that is connected to your current GitHub repo and delete the rest. In Azure Portal → **Static Web Apps**, select an app → **Delete**. Deletion is permanent (the app and its default URL are removed). The GitHub repo and workflow are unchanged; if that repo was the only one linked to the deleted app, you can later connect it to your remaining SWA via **Configuration** / **Deployment center**.

**Restructure (cleanup)** — To remove old folders and root .docx from the repo: (1) From the project root, run `git rm -r --cached <folder>` for each folder to remove (e.g. `docs-digital-thread`, `docs-industrial-ai`, `docx-for-conversion`, `word-backup`, `blog` — skip if a path doesn’t exist). (2) Run `git rm --cached *.docx` to remove root .docx (PowerShell). (3) `git add -A`, `git commit -m "chore: remove legacy folders and root docx"`, `git push origin main`. Keep `docs/`, `MD/`, `DOCX/`, `src/`, `static/`, `.github/`.

**Meaningful URL (custom domain)** — Azure assigns a fixed default URL (e.g. `https://mango-plant-01f14a910.1.azurestaticapps.net`) that you cannot rename. To use a meaningful address (e.g. `docs.yourcompany.com`): In your Static Web App → **Settings** → **Custom domains**, add your domain, add the CNAME or A-record as Azure instructs for DNS validation, then assign the custom domain. You need control over the domain’s DNS (e.g. in your org’s Azure DNS or external registrar). If you don't have permissions to add a custom domain, use a **custom/short link** instead (e.g. [https://go.accenture.com/devdocs](https://go.accenture.com/devdocs)) that redirects to the Azure default URL so people use one stable link.

---

## Applying a single update from SharePoint

When you change **one file** in SharePoint and want that change on GitHub and the Azure Static Web App:

1. **Download** the updated .docx from SharePoint (only that file).
2. **Replace** the existing file in the right asset folder: put it in `DOCX/IAI/`, `DOCX/Thread/`, or the matching `DOCX/<Asset>/` (overwrite the old .docx).
3. **Convert** without wiping existing markdown:
   ```bash
   python convert_docx_to_markdown.py --all --no-clear
   ```
   Or convert only that asset, e.g. `python convert_docx_to_markdown.py DOCX\IAI MD\IAI` (no `--no-clear` if that asset folder only has that one doc).
4. **If you use external media** (see MEDIA-STORAGE.md): upload any new or changed images to Azure Blob so the live site can show them:
   ```bash
   npm run upload-media
   ```
   (Set `AZURE_STORAGE_CONNECTION_STRING` and `AZURE_MEDIA_CONTAINER` in the environment if needed.)
5. **Build** to confirm the site compiles: `npm run build`.
6. **Commit and push to GitHub:**
   ```bash
   git add MD/
   git commit -m "Update doc from SharePoint: <doc or topic name>"
   git push origin main
   ```
7. **Azure:** Pushing to `main` triggers the GitHub Actions workflow; it builds and deploys to the Azure Static Web App. Check **Actions** in the repo until the run succeeds, then open your Static Web App URL to confirm the updated doc and images.

---

## Exporting markdown to Word (.docx)

When someone needs a Word version of the current doc (e.g. for offline review or to replace the file in SharePoint), you can **export** the `.md` file to a new `.docx`. This is **not** a sync that updates the original Word file in place — it creates a new Word document from the current markdown. You can then upload that `.docx` to SharePoint to replace the old file if you want Word to reflect the latest MD content.

**Single file (Pandoc):** From the project folder:

```bash
pandoc "MD/IAI/IAI_Architecture_Azure.md" -o "DOCX/IAI/IAI_Architecture_Azure.docx"
```

Use the correct path to your `.md` and the output path for the `.docx`. Create the output folder if needed. Open the generated `.docx` in Word, then upload to SharePoint or share as needed.

**Multiple files:** Use the helper script (requires Pandoc):

```bash
python scripts/export_md_to_docx.py MD/IAI DOCX/IAI
python scripts/export_md_to_docx.py MD/Thread DOCX/Thread
```

The script creates one `.docx` per `.md` in the source folder. Create the output folder first if it doesn't exist.

**Note:** The exported `.docx` does not preserve original Word-only features (comments, track changes, custom styles). It is a fresh export of the markdown content. Use it when the source of truth is the `.md` and you need a Word artifact for review or SharePoint.

---

## Reviewing converted (legacy) docs

After converting legacy Word docs to markdown, plan a **manual review** so the published pages are accurate and readable. This is especially important for docs converted in bulk or from older templates.

**What to check (per doc or per batch):**

1. **Live page** — Open the doc on the Static Web App (or run `npm start` and open locally). Confirm the **title and topic line** look correct (no duplicate big title; topic line is the main H1).
2. **Headings** — Scan the table of contents and in-page headings; fix any broken or duplicate headings in the `.md` file.
3. **Tables** — Ensure tables render as tables (not broken or raw pipe text). If a table is wrong, fix the source Word (simplify merged cells, one line per cell) and re-convert, or edit the `.md` directly.
4. **Links** — Click in-doc links; fix broken or incorrect URLs in the markdown.
5. **Images** — Confirm images load (paths like `media/...` or your external media URL). If an image is missing, add it to the repo or upload to Azure Blob and set `MEDIA_BASE_URL` as needed.
6. **Code blocks** — If the doc has JSON or code, ensure it appears in code blocks and is readable (no stray curly braces in prose).

**Tracking progress**  
Keep a simple list (e.g. in a spreadsheet or GitHub Project) of which docs have had a post-conversion review. Optionally add a front matter field (e.g. `legacy_reviewed: true`) or a small checklist file in the repo so the team knows which docs are signed off. Update the list as you complete each doc or batch.

---

## Editing markdown (team) and who can commit

Each doc page has an **Edit this page** link at the bottom so your team can edit easily. It opens that doc’s `.md` file on GitHub in edit mode; after editing, scroll down, add a commit message, and click **Commit changes** (or **Propose changes**). Only people with **write access** to the repo can commit directly; everyone else gets **Propose changes** (fork + pull request).

**Controlling who can commit:** In GitHub **Settings → Collaborators** (or **Manage access**), grant **Write** only to your doc team. Anyone without write access can still open the Edit link but will only get **Propose changes** (fork + PR), not commit to `main`. Optionally, in **Settings → Branches** add a rule for `main` to require pull request reviews. For small fixes use the Edit link; for large or Word-sourced updates use the **SharePoint → DOCX → convert** flow. Other readers use **Doc feedback** (GitHub Issues) to suggest changes.

**If a colleague doesn’t have a GitHub account:** You can’t add them as a collaborator until they have one (free at github.com). In the meantime they can send edits to someone who has write access—e.g. by email, a Word or shared doc, or a note—and that person applies the changes in the repo and commits. Once the colleague creates a GitHub account, add them under **Settings → Collaborators** so they can use the **Edit this page** link themselves.

 See **Collecting feedback (GitHub Issues)** in this job aid.

**Tracking who contributed:** Keep **CONTRIBUTORS.md** in the repo up to date. When you or a teammate add or edit docs, fix the site, or improve the conversion flow, add a row with their name and a short note (e.g. "Doc edits, IAI", "Conversion script"). See CONTRIBUTORS.md for the format.

---

## External contributors (fork + pull request)

People outside your team can propose changes without being added as collaborators. They work on a **fork** of the repo and open a **pull request**; your team reviews and merges (or requests changes). No write access to your repo is required for them.

**Steps for the external contributor**

1. **Fork the repo** — On GitHub, open your repo (e.g. `https://github.com/ezo001/dev-docs`), click **Fork**, and create the fork under their account or org.
2. **Clone their fork** and create a branch:
   ```bash
   git clone https://github.com/TheirUsername/dev-docs.git
   cd dev-docs
   git checkout -b fix-doc-xyz
   ```
3. **Edit** the markdown (e.g. under `MD/IAI/` or `MD/Thread/`), then commit and push to **their fork**:
   ```bash
   git add MD/IAI/Some_Doc.md
   git commit -m "Fix typo in Some Doc"
   git push origin fix-doc-xyz
   ```
4. **Open a pull request** — On GitHub, go to their fork, click **Compare & pull request** (or use **Contribute → Open pull request** from the main repo), and create a PR from `TheirUsername:fix-doc-xyz` into your repo’s `main` (or the branch you publish from). Add a short description of the change.

**Steps for your team**

1. In your repo, go to **Pull requests** and open the new PR.
2. **Review** the diff (and the built site if you have a preview), add comments or request changes if needed.
3. **Approve** when ready, then **Merge** the PR. Only people with merge rights on your repo can merge; after merge, the change is on `main` and the next deploy will publish it.
4. Optionally add the contributor to **CONTRIBUTORS.md** and close the PR.

**Optional: require PRs for everyone (including your team)**  
In **Settings → Branches**, add a rule for `main`: enable **Require a pull request before merging** (and optionally **Require approvals**). Then even collaborators must open a PR for changes to `main`; no direct pushes. Useful if you want all edits to go through review.

---

## Doc usage and analytics

To see **which docs are used most** and **how useful** they are, you can enable one or both of the following.

### Page views and traffic (which docs are used most)

- **Option A — Google Analytics 4 (GA4):**  
  Create a GA4 property at [analytics.google.com](https://analytics.google.com), get your Measurement ID (format `G-XXXXXXXXXX`). This project is already set up to use it: set **GA4_MEASUREMENT_ID** in the environment where the site is built (e.g. Azure Static Web App → **Configuration** → **Application settings** → add `GA4_MEASUREMENT_ID` = `G-XXXXXXXXXX`). The gtag plugin in `docusaurus.config.js` only runs when that variable is set, so the build works without it. After deployment, GA4 will show page views, top pages, and sessions; use **Reports → Engagement → Pages and screens** to see which docs are used most.

- **Option B — Azure Application Insights:**  
  If your site is on Azure Static Web Apps, you can enable **Application Insights** on the Static Web App (Azure Portal → your SWA → **Application Insights** → enable). You get request logs and basic metrics. For a client-rendered docs site, GA4 (or another client-side analytics tool) usually gives clearer “which doc page” data; App Insights is still useful for availability and server-side metrics.

### Usefulness (useful vs not useful)

- **Explicit feedback:** Use the existing **Doc feedback** (GitHub Issues) and ask readers to say whether the doc was helpful or what was missing. You can add a “Was this helpful?” link at the bottom of each doc that opens the Doc feedback issue template with the doc name pre-filled.
- **Optional “Was this helpful?” widget:** A small Yes/No component that posts to a form (e.g. Microsoft Forms, Google Form) or to an API that stores page path + Yes/No can be added later if you want structured usefulness metrics without opening GitHub.

Once you choose an option (e.g. GA4 + Doc feedback), add the setup steps you used to this section so your team can repeat or change it.

---

## Build and deploy commands (summary)

From the project folder:

1. **Build** the site (required before deploy):
   ```bash
   npm run build
   ```
2. **Deploy** by pushing to the branch that triggers the workflow (usually `main`). Deployment runs automatically in GitHub Actions; there is no separate deploy command to run locally.
   ```bash
   git add MD/
   git commit -m "Add/update docs from SharePoint DOCX conversion"
   git pull origin main
   git push origin main
   ```
   **If the remote has new commits**, run `git pull origin main` *before* pushing. When Git opens an editor (e.g. **nano**) for the merge commit message: keep or edit the default message, then **save** (in nano: **Ctrl+O**, then **Enter**) and **exit** (**Ctrl+X**). Then run `git push origin main`.
3. In GitHub, open **Actions** and wait for the workflow to succeed. The Azure Static Web App will then show your changes.

If you use external media (see MEDIA-STORAGE.md), run `npm run upload-media` before building. When building in CI, set `MEDIA_BASE_URL` (and `MEDIA_SAS` if the container is private).

---

## Quick reference

| Step | Action |
|------|--------|
| 1 | Download .docx from SharePoint (and extract from .zip if needed). |
| 2 | Put .docx in `DOCX/<Asset>/` (e.g. DOCX/IAI, DOCX/Thread). See ASSETS-FOLDER-GUIDE.md. |
| 2b | **Before converting:** Run Word macros/validator; avoid merged tables, smart quotes, curly braces, angle-bracketed URLs. See **Before converting: Word do's and don'ts** and WORD-TO-MDX-CHECKLIST.md. |
| 3 | Run `python convert_docx_to_markdown.py --all` (or run per-asset with paths). Use `--all --no-clear` to only add/update. |
| 4 | Run `npm start` and review the new docs in the browser. |
| 5 | Run `npm run build` to verify the site builds. If using external media, run `npm run upload-media` after converting. |
| 6 | `git add MD/` (or your output folder), `git commit`, `git push origin main`. |
| 7 | Check GitHub Actions until the deployment workflow succeeds. |
| 8 | Open your Azure Static Web App URL and confirm the docs are live. |

---

## Troubleshooting

- **Push rejected: "Updates were rejected because the remote contains work that you do not have locally"** — The remote branch has commits you don't have (e.g. from the GitHub web editor or another machine). Run `git pull origin main` to bring those changes in and merge them with yours. If Git opens a text editor (e.g. **nano**) for the merge commit message: the default message is fine; **save** (nano: **Ctrl+O**, then **Enter**) and **exit** (**Ctrl+X**) to complete the merge. Then run `git push origin main` again.
- **“Pandoc not found”** — Install Pandoc and ensure it’s on your PATH ([pandoc.org/installing](https://pandoc.org/installing.html)).
- **“No .docx files found”** — Check the path you entered; use a full path if the script doesn’t find the folder.
- **Broken images** — Ensure the conversion script ran with the correct output folder so that `docs/media/` (or your output folder’s `media/`) contains the extracted images and the .md files reference them correctly.
- **Build or MDX errors** — Fix the reported file/line (e.g. stray `{` or `<` in prose). Re-run `npm run build` after edits.
- **Deployment fails: "The size of the app content was too large" (500 MB limit)** — Azure Static Web Apps Standard plan allows 500 MB per environment. **Preferred:** Use **external media storage** so doc images are served from Azure Blob Storage instead of being bundled. See **MEDIA-STORAGE.md** for setup: create a blob container, run `npm run upload-media`, set `MEDIA_BASE_URL` when building (and in GitHub Actions), then the build stays under the limit and you can add more assets (A4E, A4M, etc.). Alternatives: (1) Bulk-compress images: `pip install Pillow`, then `python compress_media_images.py`. (2) Temporarily comment out one `@docusaurus/plugin-content-docs` block to reduce size (not ideal if you need all assets).
- **Deployment fails in GitHub Actions** — Confirm the repo has the correct Azure secret (e.g. `AZURE_STATIC_WEB_APPS_API_TOKEN_PURPLE_STONE_022C91210` for the dev-docs SWA). In Azure → your Static Web App → **Overview** → **Manage deployment token**, copy the token; in GitHub → repo **Settings** → **Secrets and variables** → **Actions**, add a secret with the exact name shown in the workflow YAML. Also ensure `output_location` in the workflow is `build` to match Docusaurus.
- **404 on Azure Static Web App (all routes)** — The site is a SPA: the fallback must serve `index.html` so the client router can handle `/`, `/digital-thread/...`, `/industrial-ai/...`, etc. In `staticwebapp.config.json`, set `navigationFallback.rewrite` to `"/index.html"` (not `"/404.html"`). A copy of the config in `static/` is included so it is deployed in the `build/` output.
- **`git add -A` or `git add MD/` seems hung (cursor flashing or stuck on warnings)** — (1) Git may still be working; with 2500+ files it can take 1–2 minutes. (2) On Windows, "LF will be replaced by CRLF" warnings can flood the terminal and look like a freeze. To stop those warnings in this repo: `git config core.autocrlf false`. (3) If it still seems stuck, add in smaller chunks (see next bullet).
- **`git add MD/` seems hung (cursor flashing)** — Adding the whole `MD/` tree can take a long time. In a **second** PowerShell window, run `Test-Path .git\index.lock`; if it returns `True`, Git is still working (or stuck). To add in smaller chunks: (1) Press **Ctrl+C** in the window where `git add` is running. (2) Remove the lock: `Remove-Item .git\index.lock -Force -ErrorAction SilentlyContinue`. (3) Add by asset folder: `git add MD/IAI/`, then `git add MD/Thread/`. Add any other asset folders under `MD/` as needed. Add any root-level `.md` in `MD/` if needed (e.g. `git add MD/*.md`). (4) Run `git status` to confirm.
- **“JavaScript heap out of memory” when running `npm start` or `npm run build`** — The site’s size can exceed Node’s default memory limit. The `package.json` scripts already set a higher limit (8 GB). If it still fails, set a larger limit before running:  
  **PowerShell:** `$env:NODE_OPTIONS="--max-old-space-size=8192"; npm start`  
  **Cmd:** `set NODE_OPTIONS=--max-old-space-size=8192 && npm start`  
  Increase `8192` (MB) if you have enough RAM (e.g. `16384` for 16 GB).
- **`npm start` is very slow (e.g. 3+ minutes)** — With 170+ docs, the first compile is heavy. The project enables webpack **filesystem cache**, so the **second and later** runs of `npm start` should be noticeably faster (2–5×) as long as you don’t run `npm run clear` or delete `node_modules/.cache`. If it’s still slow after a few runs, try: (1) Close other apps to free RAM/CPU. (2) Run `npm run clear` once, then `npm start` again to rule out a bad cache. (3) For quick iteration, temporarily comment out one or two `@docusaurus/plugin-content-docs` blocks in `docusaurus.config.js` so fewer assets are loaded in dev.
- **Wrong Git identity or wrong repo** — (1) **Identity:** Set your name and email before committing so commits aren't attributed to the auto-configured user: `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`. To fix the **last** commit's author after setting config: `git commit --amend --reset-author --no-edit`, then `git push --force-with-lease origin main`. (2) **Repo:** Confirm where you're pushing: run `git remote -v`; the `origin` URL (e.g. `https://github.com/ezo001/dev-docs.git`) is where `git push origin main` sends code. The Azure Static Web App deploys from the **GitHub repo connected in Azure** (Azure Portal → your Static Web App → **Configuration** or **Deployment source**). If that connected repo is different from `origin` (e.g. the SWA is linked to **eolson1967** but you push to **ezo001**), your push did not trigger that app's deployment. Either change `origin` to the correct repo (`git remote set-url origin https://github.com/OWNER/REPO.git`) or add a second remote and push to it.

---

## Search

The site uses **local keyword search**: the index is built at build time and search runs in the browser, so content never leaves your environment. Do **not** use Algolia or other cloud search for internal-only docs.

- **Plugin:** `@easyops-cn/docusaurus-search-local` (configured in `docusaurus.config.js`).
- **How to use:** Click the search icon in the top navbar (or use the keyboard shortcut if configured), type keywords, and choose a result. Search covers the landing docs (`docs/`), Industrial AI (`MD/IAI`), and Digital Thread (`MD/Thread`).
- **Rebuilding:** After adding or changing docs, run `npm run build` (and deploy) so the search index is regenerated.

---

## Collecting feedback (GitHub Issues)

Documentation feedback is collected as **GitHub Issues** in this repo so every submission is a trackable change request (CR) in Git. No Forms or Power Automate.

**How the reader triggers a CR**

The reader needs a **link** that opens the GitHub "new issue" page with the Doc feedback template. You add this link to the published docs (or site layout) so that from the doc they can start a CR in one click.

1. **Where to put the link** — In the Docusaurus site: footer, sidebar, or a "Send feedback" / "Report an issue" block on each doc or section. Choose one place and keep it consistent.
2. **Link target** — Use this URL (replace `OWNER` and `REPO` with your GitHub username and repo name):
   ```
   https://github.com/OWNER/REPO/issues/new?template=doc-feedback.yaml
   ```
   That URL opens the **New issue** form with the **Doc feedback** template already selected; the reader only fills in the fields and submits.
3. **Optional: pre-fill document name** — To make it easier for the reader, you can pass the current doc title into the form. Add `&document-name=Your+Doc+Title` (URL-encoded) to the link. Example: a "Feedback on this page" link on a specific doc could use the doc title so the reader doesn’t have to type it.

**How to submit feedback** (what the reader does after clicking the link)

1. In the repo that holds this project (see note below), go to **Issues** → **New issue**.
2. Choose the **Doc feedback** template.
3. Fill in the fields (document name, product, version, feedback text, etc.).
4. Add the **docs-feedback** label if it isn't already applied (the template applies it by default).
5. Optionally drag and drop screenshots or other files into the issue.
6. Submit the issue.

**Template fields** (same as the previous Forms-based flow):

| Field | Purpose |
|-------|--------|
| Document name | Name of the document this feedback is about. |
| Product / application | AOT, IX Gen AI, IX Digital Thread, ADAPT, MTAS, EDD, IEMP, or IEMP KG. |
| Document version | Version from the document footer. |
| Feedback | Free-text description of the issue or suggestion. |
| Is this about an issue? | Yes/No — accessing or using the document. |
| Attachments | Drag and drop files into the issue. |
| Where accessed | IX Developer Hub, Doc Team SharePoint, or email. |
| May the Doc Team contact you? | Yes/No. |

The issue template is in `.github/ISSUE_TEMPLATE/doc-feedback.yaml`. When directing readers to submit feedback, link to the repo's **New issue** page and ask them to use the **Doc feedback** option. Ensure the **docs-feedback** label exists in the repo (Issues → Labels → New label); the template applies it by default.

**Which repo?** The folder on your PC (e.g. `Desktop\my-docs`) is just a **local project folder**. The actual GitHub repo has its own name. To see which repo this project uses: in the project folder run `git remote -v`. You’ll see one or more remotes (e.g. `origin` → `github.com/ezo001/dev-docs.git`). That repo name (e.g. **dev-docs**) is where Issues and the Doc feedback template live after you push. Use that **OWNER/REPO** in the feedback link URL.

## Related documentation

- **CONTRIBUTORS.md** — List of people who contributed to the repo and Doc Team contact; update it when you or teammates add or edit docs or tooling.
- **WORD-TO-MDX-CHECKLIST.md** — Pre-conversion checklist for Word authors and the Doc Team (tables, quotes, braces, macros). Use before running the conversion script.
- **ASSETS-FOLDER-GUIDE.md** — How to organize `DOCX/` and `MD/` by asset (Thread, IAI, etc.) and add or retire assets without editing config.
- **MEDIA-STORAGE.md** — Serve doc images from Azure Blob Storage so the Static Web App build stays under 500 MB; required when publishing many assets (IAI, Digital Thread, A4E, A4M, etc.).
- **scripts/export_md_to_docx.py** — Export .md files to .docx (Pandoc). See **Exporting markdown to Word (.docx)** in this job aid.



