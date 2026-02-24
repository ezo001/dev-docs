/**
 * Remark plugin: rewrite relative ./media/... image URLs to an external base URL.
 * Used so doc images are served from Azure Blob Storage (or CDN), keeping the
 * Static Web App build under the 500 MB limit.
 *
 * Set MEDIA_BASE_URL (or pass baseUrl in options). When set, images like
 * ./media/IAI_Architecture_Azure/image2.png become
 * {baseUrl}/industrial-ai/IAI_Architecture_Azure/image2.png
 * (asset is inferred from the source file path: MD/IAI -> industrial-ai, MD/Thread -> digital-thread).
 *
 * For private containers (when org policy blocks anonymous access), set MEDIA_SAS (or pass sasQuery in options)
 * to a read-only container SAS query string (e.g. "sv=2021-06-08&se=...&sr=c&sp=r&sig=..."). It is appended to
 * each image URL so the browser can load blobs without anonymous access.
 *
 * Must be added as beforeDefaultRemarkPlugins so it runs before Docusaurus's
 * transformImage (which would otherwise bundle the file).
 */

import { visit } from 'unist-util-visit';

function inferAsset(filePath) {
  if (!filePath) return null;
  const normalized = filePath.replace(/\\/g, '/');
  if (normalized.includes('MD/IAI/')) return 'industrial-ai';
  if (normalized.includes('MD/Thread/')) return 'digital-thread';
  // Future: MD/A4E -> agents-engineering, MD/A4M -> agents-manufacturing, etc.
  return null;
}

/**
 * @param {{ baseUrl?: string, sasQuery?: string }} options
 * @returns {import('unified').Transformer}
 */
export default function remarkExternalMedia(options = {}) {
  const baseUrl = (options?.baseUrl ?? process.env.MEDIA_BASE_URL ?? '').replace(/\/$/, '');
  const sasQuery = (options?.sasQuery ?? process.env.MEDIA_SAS ?? '').replace(/^\?/, '');
  if (!baseUrl) return (tree) => {};

  return (tree, vfile) => {
    const filePath = vfile?.path ?? vfile?.history?.[0] ?? '';
    const asset = inferAsset(filePath);
    if (!asset) return;

    visit(tree, 'image', (node) => {
      let url = node.url || '';
      let rest = '';
      if (url.startsWith('./media/')) rest = url.slice('./media/'.length);
      else if (url.startsWith('media/')) rest = url.slice('media/'.length);
      else return;
      const fullUrl = `${baseUrl}/${asset}/${rest}`;
      node.url = sasQuery ? `${fullUrl}?${sasQuery}` : fullUrl;
    });
  };
}
