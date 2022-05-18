import React from 'react';
import { Box, Container, CssBaseline, Typography } from '@mui/material';
import { GetServerSideProps } from 'next';

export default function Home() {
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
        </Container>
      </Box>
    </Box>
  );
}

export const getServerSideProps: GetServerSideProps = async ctx => {
  return {
    props: {},
  };
};
