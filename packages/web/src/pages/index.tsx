import React from 'react';
import {
  Avatar,
  Box,
  Button,
  Checkbox,
  CssBaseline,
  FormControlLabel,
  Grid,
  Paper,
  TextField,
  Typography,
} from '@mui/material';
import Logo from '../assets/logo.jpeg';
import { LockOutlined } from '@mui/icons-material';

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
          backgroundImage: `url(${Logo.src})`,
          backgroundRepeat: 'no-repeat',
          backgroundColor: t =>
            t.palette.mode === 'light'
              ? t.palette.grey[50]
              : t.palette.grey[900],
          backgroundSize: 'cover',
          backgroundPosition: 'center',
        }}
      />
      <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
        <Typography
          variant="h2"
          component="h1"
          align="center"
          gutterBottom
          color={'#132f4c'}
        >
          Fast Entregas
        </Typography>
        <Box
          sx={{
            my: 8,
            mx: 4,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlined />
          </Avatar>
          <Typography component="h1" variant="h5">
            Login
          </Typography>
          <Box component="form" noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="telephone"
              label="Telefone"
            />
            <TextField
              margin="normal"
              required
              fullWidth
              id="password"
              label="Senha"
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Lembrar de mim"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
              href="/dashboard"
            >
              Entrar
            </Button>
          </Box>
        </Box>
      </Grid>
    </Grid>
  );
}
