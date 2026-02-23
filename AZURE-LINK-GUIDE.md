# Step 1: Link Azure Static Web App to GitHub (eolson1967/docusaurus-foundations)

Azure cannot switch an existing Static Web App to a **different** GitHub repo from the portal. You have two paths.

---

## Option A — Create a new Static Web App linked to docusaurus-foundations (recommended)

Use this if you want a clean setup or the current Azure app was created from another repo.

### 1. Open Azure Portal and create a new Static Web App

1. Go to [https://portal.azure.com](https://portal.azure.com) and sign in.
2. Search for **Static Web App** (or go to **Create a resource** → search "Static Web App").
3. Click **Create**.

### 2. Basics tab — connect to GitHub

1. **Subscription** – Choose your subscription.
2. **Resource group** – Use an existing one or create one (e.g. `rg-docs`).
3. **Name** – e.g. `docusaurus-foundations`.
4. **Plan type** – Free or Standard, as needed.
5. **Region** – Pick a region close to you.
6. **Deployment details** – Choose **GitHub** (not "Other").
7. Click **Sign in with GitHub** and authorize Azure if prompted.
8. Set:
   - **Organization:** `eolson1967`
   - **Repository:** `docusaurus-foundations`
   - **Branch:** `main`
9. Click **Review + create**, then **Create**.

Azure will create the app and add a GitHub Actions workflow to **eolson1967/docusaurus-foundations**. When you connect via the portal, the deployment token is usually added as a GitHub Actions secret **automatically**—you typically do not need to add it yourself.

After the first push to `main`, the workflow will run and deploy. Your app URL will be shown in the Azure overview (e.g. `https://<name>.azurestaticapps.net`).

**If deployments fail** with an auth error, add the secret manually: open your Static Web App in the portal → **Manage deployment token** → Copy; then in the repo go to **Settings** → **Secrets and variables** → **Actions** and create a secret with the name from the workflow file's `azure_static_web_apps_api_token` line, and paste the token as the value.

---

## Option B — Reconnect an existing Static Web App to docusaurus-foundations (Azure CLI)

Use this if you already have a Static Web App and want it to build from **eolson1967/docusaurus-foundations** instead of its current repo. The portal does not allow changing the repo; you must use the CLI.

### 1. Install and sign in to Azure CLI

- Install: [https://docs.microsoft.com/en-us/cli/azure/install-azure-cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)
- In a terminal run:
  ```bash
  az login
  ```

### 2. Disconnect the current GitHub source

Replace `<resource-group>` and `<static-web-app-name>` with your resource group and Static Web App name (from the Azure portal).

```bash
az staticwebapp disconnect --name <static-web-app-name> --resource-group <resource-group>
```

### 3. Reconnect to docusaurus-foundations

You need a **deployment token** for this app (portal → your Static Web App → **Manage deployment token** → Copy).

```bash
az staticwebapp connect \
  --name <static-web-app-name> \
  --resource-group <resource-group> \
  --source https://github.com/eolson1967/docusaurus-foundations \
  --branch main \
  --token <paste-your-deployment-token>
```

When prompted, complete GitHub sign-in/authorization so Azure can access the repo.

### 4. Workflow and secret in docusaurus-foundations

After reconnecting, Azure may add or update a workflow in **eolson1967/docusaurus-foundations**. Ensure:

- The repo has a workflow under `.github/workflows/` that uses `Azure/static-web-apps-deploy@v1`.
- The workflow's `azure_static_web_apps_api_token` uses a GitHub secret name that exists in **eolson1967/docusaurus-foundations** (e.g. `AZURE_STATIC_WEB_APPS_API_TOKEN_...`).
- In the repo: **Settings** → **Secrets and variables** → **Actions** → add a secret with that exact name and the deployment token value.

Then push to `main` to trigger a deploy.

---

## Check which repo is linked (Azure Portal)

1. Go to [https://portal.azure.com](https://portal.azure.com).
2. Search **Static Web Apps** and open your app.
3. In the left menu, open **Configuration** (or **Overview** and look for deployment/source info).
4. You'll see the linked **GitHub repository** and **branch**. That is the repo/branch Azure builds from.

---

## Summary

- **Option A:** Create a new Static Web App, choose **GitHub** and select **eolson1967/docusaurus-foundations** and **main**. Add the deployment token as the GitHub Actions secret shown in the new workflow file.
- **Option B:** Use `az staticwebapp disconnect` then `az staticwebapp connect` to point the existing app at **https://github.com/eolson1967/docusaurus-foundations** and **main**, then ensure the workflow and secret exist in that repo.

After the link is correct, push your code to `main` on **eolson1967/docusaurus-foundations** and Azure will deploy from that repo.
