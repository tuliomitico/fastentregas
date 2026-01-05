'use client';
import React from 'react';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { EmotionCacheProvider } from '../EmotionCache';

const theme = createTheme({
  spacing: 8,
});

export default function ThemeRegistry({
  children,
}: {
  children: React.ReactNode;
}): JSX.Element {
  return (
    <EmotionCacheProvider options={{ key: 'mui' }}>
      <CssBaseline />
      <ThemeProvider theme={theme}>{children}</ThemeProvider>
    </EmotionCacheProvider>
  );
}
