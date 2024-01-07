import React from 'react';
import {
  AppBar,
  CssBaseline,
  Toolbar,
  Container,
  Typography,
} from '@mui/material';
import { Moped } from '@mui/icons-material';

export default function About(): React.ReactElement {
  return (
    <>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar>
          <Moped sx={{ mr: 2, color: '#FFE66D' }} />
        </Toolbar>
      </AppBar>
      <Container>
        <Typography>Sobre nós</Typography>
      </Container>
    </>
  );
}
