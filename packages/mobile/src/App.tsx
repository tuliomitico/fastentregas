import React from 'react';
import { ThemeProvider } from 'styled-components/native';

import Home from './screens/Home';
import light from './theme/light';
import dark from './theme/dark';

export default function App() {
  return (
    <ThemeProvider theme={light}>
      <Home />
    </ThemeProvider>
  );
}
