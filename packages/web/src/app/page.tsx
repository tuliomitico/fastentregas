import React from 'react';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';

export default async function Home() {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      {/* <CssBaseline /> */}
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
