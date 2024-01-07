import React from 'react';
import ThemeRegistry from '../components/ThemeRegistry';
import StyledComponentsRegistry from '../lib/registry';
import AppProvider from '../hooks';

export default function RootLayout(props: { children: React.ReactNode }) {
  const { children } = props;
  return (
    <html lang="en">
      <body>
        <StyledComponentsRegistry>
          <ThemeRegistry>
            <AppProvider>{children}</AppProvider>
          </ThemeRegistry>
        </StyledComponentsRegistry>
      </body>
    </html>
  );
}
