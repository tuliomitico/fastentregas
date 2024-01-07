import React, { ComponentProps } from 'react';
import Link from 'next/link';
import { Typography } from '@mui/material';

export default function Copyright(
  props: ComponentProps<typeof Typography>,
): React.ReactElement {
  return (
    <Typography
      variant="body2"
      color="text.secondary"
      align="center"
      {...props}
    >
      {'Copyright © '}
      <Link href={'/'} style={{ color: 'inherit' }}>
        Fast Entregas
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}
