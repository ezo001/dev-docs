# Job Aid: SharePoint DOCX → Static Web App (Markdown)

This guide walks you from downloading Word documents from SharePoint through to having them published as markdown on your Azure Static Web App.

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

Use the **DOCX / MD** layout so you can add or retire assets (Thread, IAI, AOT, etc.) without editing config. See **ASSETS-FOLDER-GUIDE.md** for full details.

1. Open the folder where your Docusaurus project lives (e.g. `my-docs`).
2. Put source .docx files in **DOCX** under a subfolder for that asset:
   - **Digital Thread** → `DOCX/Thread/`
   - **Industrial AI** → `DOCX/IAI/`
   - **New asset (e.g. AOT)** → create `DOCX/AOT/` and put .docx there.
3. Put **only** the .docx files you want to convert in that asset folder (no fixed list to maintain).

**Example layout:**

```
my-docs/
├── DOCX/               ← Source Word files (one subfolder per asset)
│   ├── Thread/        ← Digital Thread .docx
│   ├── IAI/           ← Industrial AI .docx
│   └── AOT/           ← (optional) add when needed
├── MD/                 ← Converted markdown (same subfolder names)
│   ├── Thread/
│   ├── IAI/
│   └── AOT/
├── convert_docx_to_markdown.py
└── package.json
```

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

**Meaningful URL (custom domain)** — Azure assigns a fixed default URL (e.g. `https://mango-plant-01f14a910.1.azurestaticapps.net`) that you cannot rename. To use a meaningful address (e.g. `docs.yourcompany.com`): In your Static Web App → **Settings** → **Custom domains**, add your domain, add the CNAME or A-record as Azure instructs for DNS validation, then assign the custom domain. You need control over the domain’s DNS (e.g. in your org’s Azure DNS or external registrar).

---

## Quick reference

| Step | Action |
|------|--------|
| 1 | Download .docx from SharePoint (and extract from .zip if needed). |
| 2 | Put .docx in `DOCX/<Asset>/` (e.g. DOCX/IAI, DOCX/Thread). See ASSETS-FOLDER-GUIDE.md. |
| 3 | Run `python convert_docx_to_markdown.py --all` (or run per-asset with paths). |
| 4 | Run `npm start` and review the new docs in the browser. |
| 5 | Run `npm run build` to verify the site builds. |
| 6 | `git add docs/` (or your output folder), `git commit`, `git push origin main`. |
| 7 | Check GitHub Actions until the deployment workflow succeeds. |
| 8 | Open your Azure Static Web App URL and confirm the docs are live. |

---

## Troubleshooting

- **“Pandoc not found”** — Install Pandoc and ensure it’s on your PATH ([pandoc.org/installing](https://pandoc.org/installing.html)).
- **“No .docx files found”** — Check the path you entered; use a full path if the script doesn’t find the folder.
- **Broken images** — Ensure the conversion script ran with the correct output folder so that `docs/media/` (or your output folder’s `media/`) contains the extracted images and the .md files reference them correctly.
- **Build or MDX errors** — Fix the reported file/line (e.g. stray `{` or `<` in prose). Re-run `npm run build` after edits.
- **Deployment fails in GitHub Actions** — Confirm the repo has the correct Azure secret (e.g. `AZURE_STATIC_WEB_APPS_API_TOKEN_PURPLE_STONE_022C91210` for the dev-docs SWA). In Azure → your Static Web App → **Overview** → **Manage deployment token**, copy the token; in GitHub → repo **Settings** → **Secrets and variables** → **Actions**, add a secret with the exact name shown in the workflow YAML. Also ensure `output_location` in the workflow is `build` to match Docusaurus.
- **404 on Azure Static Web App (all routes)** — The site is a SPA: the fallback must serve `index.html` so the client router can handle `/`, `/aot/...`, etc. In `staticwebapp.config.json`, set `navigationFallback.rewrite` to `"/index.html"` (not `"/404.html"`). A copy of the config in `static/` is included so it is deployed in the `build/` output.
- **`git add -A` or `git add MD/` seems hung (cursor flashing or stuck on warnings)** — (1) Git may still be working; with 2500+ files it can take 1–2 minutes. (2) On Windows, "LF will be replaced by CRLF" warnings can flood the terminal and look like a freeze. To stop those warnings in this repo: `git config core.autocrlf false`. (3) If it still seems stuck, add in smaller chunks (see next bullet).
- **`git add MD/` seems hung (cursor flashing)** — Adding the whole `MD/` tree can take a long time. In a **second** PowerShell window, run `Test-Path .git\index.lock`; if it returns `True`, Git is still working (or stuck). To add in smaller chunks: (1) Press **Ctrl+C** in the window where `git add` is running. (2) Remove the lock: `Remove-Item .git\index.lock -Force -ErrorAction SilentlyContinue`. (3) Add by asset folder: `git add MD/AOT/`, then `git add MD/IAI/`, then `git add MD/Thread/`. Add any root-level `.md` in `MD/` if needed (e.g. `git add MD/*.md`). (4) Run `git status` to confirm.
- **“JavaScript heap out of memory” when running `npm start` or `npm run build`** — The site’s size can exceed Node’s default memory limit. The `package.json` scripts already set a higher limit (8 GB). If it still fails, set a larger limit before running:  
  **PowerShell:** `$env:NODE_OPTIONS="--max-old-space-size=8192"; npm start`  
  **Cmd:** `set NODE_OPTIONS=--max-old-space-size=8192 && npm start`  
  Increase `8192` (MB) if you have enough RAM (e.g. `16384` for 16 GB).
- **`npm start` is very slow (e.g. 3+ minutes)** — With 170+ docs, the first compile is heavy. The project enables webpack **filesystem cache**, so the **second and later** runs of `npm start` should be noticeably faster (2–5×) as long as you don’t run `npm run clear` or delete `node_modules/.cache`. If it’s still slow after a few runs, try: (1) Close other apps to free RAM/CPU. (2) Run `npm run clear` once, then `npm start` again to rule out a bad cache. (3) For quick iteration, temporarily comment out one or two `@docusaurus/plugin-content-docs` blocks in `docusaurus.config.js` so fewer assets are loaded in dev.
- **Wrong Git identity or wrong repo** — (1) **Identity:** Set your name and email before committing so commits aren't attributed to the auto-configured user: `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`. To fix the **last** commit's author after setting config: `git commit --amend --reset-author --no-edit`, then `git push --force-with-lease origin main`. (2) **Repo:** Confirm where you're pushing: run `git remote -v`; the `origin` URL (e.g. `https://github.com/ezo001/dev-docs.git`) is where `git push origin main` sends code. The Azure Static Web App deploys from the **GitHub repo connected in Azure** (Azure Portal → your Static Web App → **Configuration** or **Deployment source**). If that connected repo is different from `origin` (e.g. the SWA is linked to **eolson1967** but you push to **ezo001**), your push did not trigger that app's deployment. Either change `origin` to the correct repo (`git remote set-url origin https://github.com/OWNER/REPO.git`) or add a second remote and push to it.

---

## Search (to add later)

The site must have keyword search. Use a **local / client-side** search solution so that content never leaves your environment (index built at build time, search runs in the browser). Do **not** use Algolia or other cloud search for internal-only docs, as they crawl and store your content on external servers.

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

- **ASSETS-FOLDER-GUIDE.md** — How to organize `DOCX/` and `MD/` by asset (Thread, IAI, AOT, etc.) and add or retire assets without editing config.


