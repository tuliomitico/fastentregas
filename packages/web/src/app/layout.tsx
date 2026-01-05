import React from 'react';
import { AppRouterCacheProvider } from '@mui/material-nextjs/v14-appRouter';

import ThemeRegistry from '../components/ThemeRegistry';
import StyledComponentsRegistry from '../lib/registry';
import AppProvider from '../hooks';

export default function RootLayout(props: { children: React.ReactNode }) {
  const { children } = props;
  return (
    <html lang="en">
      <body>
        <AppRouterCacheProvider>
          <StyledComponentsRegistry>
            <ThemeRegistry>
              <AppProvider>{children}</AppProvider>
            </ThemeRegistry>
          </StyledComponentsRegistry>
        </AppRouterCacheProvider>
      </body>
    </html>
  );
}
