import React from 'react';
import Layout from '../../components/Layout';

export default function RootLayout(props: { children: React.ReactNode }) {
  const { children } = props;
  return <Layout>{children}</Layout>;
}
