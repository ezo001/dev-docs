# Doc images in external storage (Azure Blob)

To keep the Static Web App build under Azure’s 500 MB limit while publishing many assets (IAI, Digital Thread, A4E, A4M, etc.), doc images under `MD/*/media` can be served from **Azure Blob Storage** instead of being bundled into the site.

**Access:** The documentation site is internal; only users with an **@accenture.com** address may access it. The Static Web App should be protected (e.g. Azure AD / Entra ID) so that only those users can load the site. Image URLs (including any SAS) are then only requested by browsers of users who have already passed that authentication.

## How it works

1. **Upload**: Script uploads `MD/IAI/media/*` and `MD/Thread/media/*` (and any future asset media) to a blob container with prefixes `industrial-ai/`, `digital-thread/`, etc.
2. **Build**: When `MEDIA_BASE_URL` is set, a Docusaurus remark plugin rewrites image URLs in the markdown from `./media/...` to `{MEDIA_BASE_URL}/{asset}/...`, so the built site references the blob URLs and does not include those files in the bundle.
3. **Deploy**: The Static Web App only deploys HTML/JS/CSS and no longer hits the size limit.

## One-time setup

### 1. Create Azure Storage and container

- In [Azure Portal](https://portal.azure.com), create a **Storage account** (or use an existing one).
- Create a **container** (e.g. `docs-media`).
  - If your org allows it: set **Public access level** to **Blob (anonymous read access for blobs only)** so the site can load images with no auth.
  - If a policy blocks anonymous access (e.g. "Failed to update storage account... disallowed by policy"): leave the container **private** and use a **SAS (Shared Access Signature)** instead — see [When anonymous access is blocked](#when-anonymous-access-is-blocked) below.
- Get either:
  - **Connection string**: Storage account → Access keys → Connection string, or  
  - **Account name + key**: same place.

### 2. Upload media

From the repo root:

```bash
npm install
set AZURE_STORAGE_CONNECTION_STRING=<your-connection-string>
set AZURE_MEDIA_CONTAINER=docs-media
npm run upload-media
```

Or with account + key:

```bash
set AZURE_STORAGE_ACCOUNT=<account-name>
set AZURE_STORAGE_ACCESS_KEY=<key>
set AZURE_MEDIA_CONTAINER=docs-media
npm run upload-media
```

The script prints something like:  
`Set MEDIA_BASE_URL=https://<account>.blob.core.windows.net/docs-media`

### 3. Build and deploy with external media

- **Locally**:  
  `set MEDIA_BASE_URL=https://<account>.blob.core.windows.net/docs-media`  
  then `npm run build` (or `npm start`).
- **GitHub Actions**: The workflow uses **repository variables** so the build gets the media URL (and optional SAS):
  - In GitHub: repo **Settings** → **Secrets and variables** → **Actions** → **Variables** tab.
  - Add **MEDIA_BASE_URL** = `https://<account>.blob.core.windows.net/docs-media` (your container URL).
  - If using a private container with SAS, add **MEDIA_SAS** = the SAS query string (e.g. `sv=2021-06-08&se=2026-12-31&sr=c&sp=r&sig=...`). Prefer a **secret** for MEDIA_SAS so it isn’t visible in logs.
  - The workflow runs `npm run build` with these env set, then deploys the `build` folder. If `MEDIA_BASE_URL` is not set, images are bundled as before (build may exceed 500 MB).

You do **not** need to upload on every build unless you add or change images. Re-run `npm run upload-media` when you add new docs or update images, then commit and push as usual.

### When anonymous access is blocked

If an Azure Policy prevents enabling Blob anonymous access (e.g. "Resource 'devdocsmedia' was disallowed by policy"):

1. **Leave the container private** — do not enable anonymous access.
2. **Create a container SAS** with read-only access:
   - In the portal: open your container → **Shared access signature** (left menu or ⋮).
   - Set **Signing key** to Key 1, **Permissions** to **Read** only, **Start and expiry** to a long window (e.g. 1–2 years), **Allowed IP addresses** blank if you want the site (and any visitor) to load images.
   - Generate the SAS and copy the **Blob SAS URL** or the **Query string** part only (the part after `?`, e.g. `sv=2021-06-08&se=2026-12-31&sr=c&sp=r&sig=...`).
3. **Set MEDIA_SAS** in addition to MEDIA_BASE_URL:
   - **Locally**: `set MEDIA_SAS=<query-string>` (the part after `?`).
   - **GitHub Actions**: Add a **secret** (not a variable) **MEDIA_SAS** with that query string, and in the workflow set `MEDIA_SAS: ${{ secrets.MEDIA_SAS }}` in the `env` block so the build can append it to every image URL.
4. The remark plugin appends this query string to each image URL so blobs are accessible without anonymous access.

**Note:** The SAS is embedded in the built HTML. Use a long expiry and rotate before it expires (re-generate SAS, update the secret, rebuild/redeploy). For maximum security with private data, consider Azure CDN with a private origin and token auth instead.

## When to re-upload

- After converting new DOCX → MD that add images under `MD/*/media`.
- After adding a new asset (e.g. A4E): add its `localDir` and `blobPrefix` in `scripts/upload-media-to-azure.js`, then run `upload-media` and extend the remark plugin’s `inferAsset()` in `src/remark/remark-external-media.js` for the new path.

## Adding a new asset (e.g. A4E, A4M)

1. **Upload script** (`scripts/upload-media-to-azure.js`): Add to the `ASSETS` array, e.g.  
   `{ localDir: path.join(ROOT, 'MD', 'A4E', 'media'), blobPrefix: 'agents-engineering' }`
2. **Remark plugin** (`src/remark/remark-external-media.js`): In `inferAsset()`, add a case for the new path, e.g.  
   `if (normalized.includes('MD/A4E/')) return 'agents-engineering';`
3. Run `npm run upload-media`, then build with `MEDIA_BASE_URL` set.

## Local dev without blob

If `MEDIA_BASE_URL` is not set, images are not rewritten and Docusaurus serves them from the repo as usual. So you can run `npm start` without any Azure config and still see local images.
