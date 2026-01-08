import React from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function Home() {
  return (
    <Layout title="AOT Documentation" description="Asset Optimization & Transformation Documentation">
      <main style={{padding: '4rem 2rem', maxWidth: '1200px', margin: '0 auto'}}>
        <h1>AOT Documentation Portal</h1>
        <p style={{fontSize: '1.2rem', marginBottom: '2rem'}}>
          Welcome to the Asset Optimization & Transformation documentation. 
          Browse our comprehensive guides and API references.
        </p>
        <Link 
          to="/docs/aot-general-architecture-auriga"
          style={{
            backgroundColor: '#2e8555',
            color: 'white',
            padding: '0.75rem 1.5rem',
            borderRadius: '4px',
            textDecoration: 'none',
            display: 'inline-block'
          }}>
          View Documentation →
        </Link>
      </main>
    </Layout>
  );
}