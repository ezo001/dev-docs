/**
 * Override: browser tab shows only the site title "DevDocs" on every page
 * (no "Page title | DevDocs").
 */
import React from 'react';
import { TitleFormatterProvider } from '@docusaurus/theme-common/internal';

const formatter = (params) => {
  return params.siteTitle;
};

export default function ThemeProviderTitleFormatter({ children }) {
  return (
    <TitleFormatterProvider formatter={formatter}>
      {children}
    </TitleFormatterProvider>
  );
}
