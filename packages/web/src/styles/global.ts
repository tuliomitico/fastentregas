import { createGlobalStyle } from 'styled-components';

export default createGlobalStyle`
  body {
    background: ${prop => prop.theme.colors.background};
  }
`;
