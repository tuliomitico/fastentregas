import React from 'react';
import AppBar from '@mui/material/AppBar';
import Moped from '@mui/icons-material/Moped';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Toolbar from '@mui/material/Toolbar';
import CssBaseline from '@mui/material/CssBaseline';

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
