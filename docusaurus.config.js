import {themes as prismThemes} from 'prism-react-renderer';

const config = {
  title: 'Docs',
  tagline: 'Documentation',
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
      },
      blog: false,
      theme: {customCss: './src/css/custom.css'},
    }],
  ],

  plugins: [
    ['@docusaurus/plugin-content-docs', {
      id: 'industrial-ai',
      path: 'docs-industrial-ai',
      routeBasePath: 'industrial-ai',
      sidebarPath: './sidebars-industrial-ai.js',
    }],
    ['@docusaurus/plugin-content-docs', {
      id: 'digital-thread',
      path: 'docs-digital-thread',
      routeBasePath: 'digital-thread',
      sidebarPath: './sidebars-digital-thread.js',
    }],
  ],

  themeConfig: {
    navbar: {
      title: 'Docs',
      items: [
        {to: '/industrial-ai/', label: 'Industrial AI', position: 'left'},
        {to: '/digital-thread/', label: 'Digital Thread', position: 'left'},
      ],
    },
    prism: {theme: prismThemes.github, darkTheme: prismThemes.dracula},
  },
};

export default config;
