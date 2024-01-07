import React from 'react';
import {
  Box,
  CssBaseline,
  Container,
  Grid,
  Typography,
  Button,
} from '@mui/material';

export default async function Home() {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      <CssBaseline />
      <Container component="main" sx={{ mt: 8, mb: 2 }} maxWidth="sm">
        <Typography component={'h1'} variant="h1" gutterBottom>
          Fast Entregas
        </Typography>
      </Container>
      <Box>
        <Container component="div" maxWidth="sm">
          <Typography component="span">
            Suas entregas, nosso compromentimento
          </Typography>
          <Grid container mt={3} spacing={3}>
            <Grid item>
              <Button variant="contained" href="/login">
                Login
              </Button>
            </Grid>
            <Grid item>
              <Button variant="contained" href="/about">
                Sobre
              </Button>
            </Grid>
          </Grid>
        </Container>
      </Box>
    </Box>
  );
}
