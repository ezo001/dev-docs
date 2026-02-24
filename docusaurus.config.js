import {themes as prismThemes} from 'prism-react-renderer';
import remarkExternalMedia from './src/remark/remark-external-media.js';

// When set, doc images under MD/*/media are served from this URL instead of being bundled.
// Use Azure Blob Storage (or CDN) to keep the Static Web App build under 500 MB.
// Optional: MEDIA_SAS = container SAS query string when anonymous access is blocked by policy.
// See scripts/upload-media-to-azure.js and MEDIA-STORAGE.md.
const MEDIA_BASE_URL = process.env.MEDIA_BASE_URL || '';
const MEDIA_SAS = process.env.MEDIA_SAS || '';

const config = {
  title: 'Docs',
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
        editUrl: 'https://github.com/eolson1967/docusaurus-foundations/edit/main/',
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
  ],

  themeConfig: {
    navbar: {
      hideOnScroll: false,
      logo: {
        alt: 'Accenture',
        src: 'img/acn-logo.png',
        srcDark: 'img/acn-logo.png',
      },
      title: 'Docs',
      items: [],
    },
    prism: {theme: prismThemes.github, darkTheme: prismThemes.dracula},
  },
};

export default config;
