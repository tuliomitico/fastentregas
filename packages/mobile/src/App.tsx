import React from 'react';
import { ThemeProvider } from 'styled-components/native';

import light from './theme/light';
import dark from './theme/dark';
import Routes from './routes/index.routes';
import AppProvider from './hooks';

export default function App() {
  return (
    <AppProvider>
      <ThemeProvider theme={dark}>
        <Routes theme={dark} />
      </ThemeProvider>
    </AppProvider>
  );
}
