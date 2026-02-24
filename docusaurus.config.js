import {themes as prismThemes} from 'prism-react-renderer';
import remarkExternalMedia from './src/remark/remark-external-media.js';

// When set, doc images under MD/*/media are served from this URL instead of being bundled.
// Use Azure Blob Storage (or CDN) to keep the Static Web App build under 500 MB.
// Optional: MEDIA_SAS = container SAS query string when anonymous access is blocked by policy.
// See scripts/upload-media-to-azure.js and MEDIA-STORAGE.md.
const MEDIA_BASE_URL = process.env.MEDIA_BASE_URL || '';
const MEDIA_SAS = process.env.MEDIA_SAS || '';
// Optional: set GA4_MEASUREMENT_ID (e.g. G-XXXXXXXXXX) in Azure SWA config or .env to enable doc usage analytics.
const GA4_MEASUREMENT_ID = process.env.GA4_MEASUREMENT_ID || '';

const config = {
  title: 'DevDocs',
  favicon: 'img/favicon.ico',
  future: {v4: true},
  url: 'https://example.com',
  baseUrl: '/',
  onBrokenLinks: 'warn',
  
  markdown: {
    hooks: {
      onBrokenMarkdownImages: ({filePath}) => {
        if (filePath && filePath.endsWith('.emf')) {
          return 'pathname://placeholder.png';
        }
      },
    },
  },

  i18n: {defaultLocale: 'en', locales: ['en']},

  presets: [
    ['classic', {
      docs: {
        path: 'docs',
        routeBasePath: '/',
        sidebarPath: './sidebars.js',
        editUrl: 'https://github.com/ezo001/dev-docs/edit/main/',
      },
      blog: false,
      theme: {customCss: './src/css/custom.css'},
    }],
  ],

  plugins: [
    // Enable webpack filesystem cache so subsequent npm start runs are much faster (2–5× after first run).
    function webpackCachePlugin() {
      return {
        name: 'webpack-cache-plugin',
        configureWebpack() {
          return {
            cache: {
              type: 'filesystem',
              buildDependencies: { config: [__filename] },
            },
          };
        },
      };
    },
    ['@docusaurus/plugin-content-docs', {
      id: 'industrial-ai',
      path: 'MD/IAI',
      routeBasePath: 'industrial-ai',
      sidebarPath: './sidebars-industrial-ai.js',
      editUrl: 'https://github.com/ezo001/dev-docs/edit/main/',
      beforeDefaultRemarkPlugins: MEDIA_BASE_URL
        ? [[remarkExternalMedia, { baseUrl: MEDIA_BASE_URL, sasQuery: MEDIA_SAS }]]
        : [],
    }],
    ['@docusaurus/plugin-content-docs', {
      id: 'digital-thread',
      path: 'MD/Thread',
      routeBasePath: 'digital-thread',
      sidebarPath: './sidebars-digital-thread.js',
      editUrl: 'https://github.com/ezo001/dev-docs/edit/main/',
      beforeDefaultRemarkPlugins: MEDIA_BASE_URL
        ? [[remarkExternalMedia, { baseUrl: MEDIA_BASE_URL, sasQuery: MEDIA_SAS }]]
        : [],
    }],
    // Local keyword search (index at build time, search in browser; no content leaves the site).
    [
      require.resolve('@easyops-cn/docusaurus-search-local'),
      {
        hashed: true,
        indexDocs: true,
        indexBlog: false,
        indexPages: false,
        docsRouteBasePath: ['/', 'industrial-ai', 'digital-thread'],
        docsDir: ['docs', 'MD/IAI', 'MD/Thread'],
        searchResultLimits: 15,
        searchResultContextMaxLength: 60,
      },
    ],
    // Doc usage analytics: only active when GA4_MEASUREMENT_ID is set (e.g. in Azure SWA env or .env).
    ...(GA4_MEASUREMENT_ID
      ? [['@docusaurus/plugin-google-gtag', { trackingID: GA4_MEASUREMENT_ID, anonymizeIP: true }]]
      : []),
  ],

  themeConfig: {
    navbar: {
      hideOnScroll: false,
      logo: {
        alt: 'Accenture',
        src: 'img/acn-logo.png',
        srcDark: 'img/acn-logo.png',
      },
      title: 'DevDocs',
      items: [
        { to: '/', label: 'Home', position: 'left' },
      ],
    },
    prism: {theme: prismThemes.github, darkTheme: prismThemes.dracula},
  },
};

export default config;
