import React from 'react';
import { CssBaseline, Grid, Typography } from '@mui/material';

export default function Home() {
  return (
    <Grid container component="main" sx={{ height: '100vh' }}>
      <CssBaseline />
      <Grid
        item
        xs={false}
        sm={4}
        md={7}
        sx={{
          backgroundImage: 'url(https://source.unsplash.com/random)',
          backgroundRepeat: 'no-repeat',
        }}
      />
      <Typography variant="h2">Fast Entregas</Typography>
    </Grid>
  );
}
