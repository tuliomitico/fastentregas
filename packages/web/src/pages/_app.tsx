import { AppProps } from 'next/app';
import React from 'react';
import { AuthProvider } from '../hooks/AuthContext';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AuthProvider>
      <Component {...pageProps} />
    </AuthProvider>
  );
}

export default MyApp;
