#!/usr/bin/env node
/**
 * Upload MD/IAI/media and MD/Thread/media to an Azure Blob Storage container.
 * Blob paths: industrial-ai/<folder>/<file>, digital-thread/<folder>/<file>
 * so that MEDIA_BASE_URL = "https://<account>.blob.core.windows.net/<container>"
 * serves images used by the remark-external-media plugin.
 *
 * Requires: npm install @azure/storage-blob
 * Env: AZURE_STORAGE_CONNECTION_STRING = full connection string from Azure Portal
 *        (Storage account → Access keys → Connection string). Do NOT use the SAS query string here.
 *      AZURE_MEDIA_CONTAINER (default: docs-media)
 *
 * Usage:
 *   node scripts/upload-media-to-azure.js
 *   AZURE_MEDIA_CONTAINER=my-container node scripts/upload-media-to-azure.js
 */

import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import {
  BlobServiceClient,
  StorageSharedKeyCredential,
} from '@azure/storage-blob';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');

const ASSETS = [
  { localDir: path.join(ROOT, 'MD', 'IAI', 'media'), blobPrefix: 'industrial-ai' },
  { localDir: path.join(ROOT, 'MD', 'Thread', 'media'), blobPrefix: 'digital-thread' },
];

function* walkDir(dir) {
  if (!fs.existsSync(dir)) return;
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) yield* walkDir(full);
    else if (e.isFile()) yield full;
  }
}

function getBlobPath(localPath, localDir, blobPrefix) {
  const relative = path.relative(localDir, localPath).replace(/\\/g, '/');
  return `${blobPrefix}/${relative}`;
}

async function uploadFile(containerClient, localPath, blobPath) {
  const blobClient = containerClient.getBlockBlobClient(blobPath);
  await blobClient.uploadFile(localPath, { blobHTTPHeaders: { blobContentType: mime(localPath) } });
}

function mime(filePath) {
  const ext = path.extname(filePath).toLowerCase();
  const map = { '.png': 'image/png', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.gif': 'image/gif', '.webp': 'image/webp', '.svg': 'image/svg+xml' };
  return map[ext] || 'application/octet-stream';
}

async function main() {
  const connectionString = process.env.AZURE_STORAGE_CONNECTION_STRING;
  const account = process.env.AZURE_STORAGE_ACCOUNT;
  const key = process.env.AZURE_STORAGE_ACCESS_KEY;
  const containerName = process.env.AZURE_MEDIA_CONTAINER || 'docs-media';

  let client;
  if (connectionString) {
    client = BlobServiceClient.fromConnectionString(connectionString);
  } else if (account && key) {
    client = new BlobServiceClient(
      `https://${account}.blob.core.windows.net`,
      new StorageSharedKeyCredential(account, key)
    );
  } else {
    console.error('Set AZURE_STORAGE_CONNECTION_STRING (from Azure Portal → Storage account → Access keys → Connection string).');
    console.error('Do not use the SAS query string; use the full connection string (starts with DefaultEndpointsProtocol=...).');
    process.exit(1);
  }

  const containerClient = client.getContainerClient(containerName);
  // Create container with no public access (private). Site uses SAS (MEDIA_SAS) to read.
  await containerClient.createIfNotExists();

  let total = 0;
  for (const { localDir, blobPrefix } of ASSETS) {
    if (!fs.existsSync(localDir)) {
      console.log('Skip (missing):', localDir);
      continue;
    }
    console.log('Uploading', localDir, '->', blobPrefix + '/');
    for (const localPath of walkDir(localDir)) {
      const blobPath = getBlobPath(localPath, localDir, blobPrefix);
      await uploadFile(containerClient, localPath, blobPath);
      total++;
      if (total % 50 === 0) process.stdout.write('.');
    }
  }
  console.log('\nDone. Uploaded', total, 'files.');
  const baseUrl = containerClient.url.replace(/\/$/, '');
  console.log('Set MEDIA_BASE_URL=' + baseUrl);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
