import React from 'react';
import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Checkbox from '@mui/material/Checkbox';
import CssBaseline from '@mui/material/CssBaseline';
import FormControlLabel from '@mui/material/FormControlLabel';
import Grid from '@mui/material/Grid';
import LockOutlined from '@mui/icons-material/LockOutlined';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import * as Yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';
import { useForm } from 'react-hook-form';
import { MaskService } from 'tp-react-web-masked-text';

import CustomTextField from '../../components/CustomTextField';
import Logo from '../../assets/logo.jpeg';
import { useAuth } from '../../hooks/AuthContext';

export default function Home() {
  const { signIn } = useAuth();
  const schema = Yup.object().shape({
    telephone: Yup.string().required('Telefone obrigatório'),
    password: Yup.string()
      .required('Senha obrigatória')
      .min(3, 'A senha dever ser maior que 8 dígitos'),
  });
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({ resolver: yupResolver(schema), mode: 'onBlur' });
  async function handleSignIn(data) {
    const { telephone, password } = data;
    const formattedTelephone = MaskService.toRawValue('cel-phone', telephone, {
      dddMask: '(99) ',
      withDDD: true,
      maskType: 'BRL',
    });
    console.log(formattedTelephone);

    await signIn({ telephone: formattedTelephone, password });
  }
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
          <Box
            component="form"
            noValidate
            sx={{ mt: 1 }}
            onSubmit={handleSubmit(handleSignIn)}
          >
            <CustomTextField
              name="telephone"
              errors={errors}
              control={control}
              inputMask
              mask={'(99) 9999-9999'}
              margin="normal"
              required
              fullWidth
              id="telephone"
              label="Telefone"
            />
            <CustomTextField
              name="password"
              errors={errors}
              control={control}
              margin="normal"
              type="password"
              required
              fullWidth
              id="password"
              autoComplete="current-password"
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
              onClick={handleSubmit(handleSignIn)}
            >
              Entrar
            </Button>
          </Box>
        </Box>
      </Grid>
    </Grid>
  );
}
