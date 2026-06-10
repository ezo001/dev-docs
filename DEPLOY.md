# Deploy portfolio to ezo001/dev-docs

This replaces everything in your personal GitHub repo with the static portfolio only.
Your work repo (`Accenture-AI-Engineering/314439_devdocs`) is **not** touched.

**Before you start:** The current `ezo001/dev-docs` history is mostly a mirror of doc work. If you want a backup, download a zip from GitHub first (Code → Download ZIP).

---

## 1. Publish files to GitHub

From PowerShell, run these commands. Use a **separate folder** so your main `my-docs` workspace stays intact.

```powershell
# Clone your personal repo
cd $env:USERPROFILE\Desktop
git clone https://github.com/ezo001/dev-docs.git dev-docs-portfolio
cd dev-docs-portfolio

# Remove old content (keep .git)
Get-ChildItem -Force | Where-Object { $_.Name -ne '.git' } | Remove-Item -Recurse -Force

# Copy portfolio files to repo root
Copy-Item -Path "C:\Users\edward.r.olson\Desktop\my-docs\portfolio\*" -Destination . -Recurse -Force

git add -A
git status
git commit -m "Repurpose repo as technical writing portfolio"
git push origin main
```

If `main` does not exist on the remote, use `master` instead, or run `git branch -M main` before push.

---

## 2. Turn on GitHub Pages

1. Open https://github.com/ezo001/dev-docs/settings/pages
2. **Source:** Deploy from a branch
3. **Branch:** `main` → `/ (root)` → Save
4. Wait 1–2 minutes. Your site will be at:

   **https://ezo001.github.io/dev-docs/**

---

## 3. Make the repo public (recommended for job search)

Portfolios are usually public so recruiters can view them without a GitHub login.

1. Settings → General → Danger zone → Change repository visibility → **Public**
2. Optional: rename the repo to `portfolio` in Settings → General. The URL becomes `https://ezo001.github.io/portfolio/`.

---

## 4. Update links after deploy

- Add the live Pages URL to your LinkedIn Featured section
- Put it on your resume
- Optionally add a “Live site” button on the portfolio (only after Pages is enabled)

---

## Keeping work and portfolio separate

| Repo | Purpose |
|------|---------|
| `Accenture-AI-Engineering/314439_devdocs` | Work — DevDocs site (private) |
| `ezo001/dev-docs` | Personal — portfolio only (public) |

Edit the portfolio in `my-docs/portfolio/`, then re-run the copy + commit + push steps when you update it.
