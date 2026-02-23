/**
 * Wrap the default Layout to show the Accenture logo at the top of the main
 * content on every page (including future docs).
 */
import React from 'react';
import Layout from '@theme-original/Layout';

export default function LayoutWrapper(props) {
  return (
    <Layout {...props}>
      <>
        <img
          src="/img/acn-logo.png"
          alt="Accenture"
          className="site-logo site-logo-global"
        />
        {props.children}
      </>
    </Layout>
  );
}
