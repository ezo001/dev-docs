/**
 * Wrap the default Layout (pass-through; logo is in the navbar only).
 */
import React from 'react';
import Layout from '@theme-original/Layout';

export default function LayoutWrapper(props) {
  return <Layout {...props}>{props.children}</Layout>;
}
