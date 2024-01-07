import React from 'react';
import { Grid, CircularProgress } from '@mui/material';

export default function Loading(): JSX.Element {
  return (
    <Grid
      container
      alignItems={'center'}
      justifyContent={'center'}
      width={'100%'}
      height={'100%'}
      marginTop={'25%'}
    >
      <CircularProgress />
    </Grid>
  );
}
