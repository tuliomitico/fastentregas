import { Link, Typography } from '@mui/material';
import React from 'react';

export default function Copyright(
  props: typeof Typography,
): React.ReactElement {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {'Copyright © '}
      <Link color="inherit" href="/">
        Fast Entregas
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}
