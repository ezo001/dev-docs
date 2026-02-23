import {themes as prismThemes} from 'prism-react-renderer';

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
    // Temporarily disabled to stay under Azure SWA 500 MB deployment limit. Re-enable after compressing images in MD/IAI/media.
    // ['@docusaurus/plugin-content-docs', {
    //   id: 'industrial-ai',
    //   path: 'MD/IAI',
    //   routeBasePath: 'industrial-ai',
    //   sidebarPath: './sidebars-industrial-ai.js',
    //   editUrl: 'https://github.com/ezo001/dev-docs/edit/main/',
    // }],
    ['@docusaurus/plugin-content-docs', {
      id: 'digital-thread',
      path: 'MD/Thread',
      routeBasePath: 'digital-thread',
      sidebarPath: './sidebars-digital-thread.js',
      editUrl: 'https://github.com/eolson1967/docusaurus-foundations/edit/main/',
    }],
    ['@docusaurus/plugin-content-docs', {
      id: 'aot',
      path: 'MD/AOT',
      routeBasePath: 'aot',
      sidebarPath: './sidebars-aot.js',
      editUrl: 'https://github.com/eolson1967/docusaurus-foundations/edit/main/',
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
