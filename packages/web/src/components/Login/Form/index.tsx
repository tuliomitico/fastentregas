'use client';
import React from 'react';
import { useForm } from 'react-hook-form';
import { yupResolver } from '@hookform/resolvers/yup';
import { Box, Button, Checkbox, FormControlLabel } from '@mui/material';
import * as Yup from 'yup';
import { MaskService } from 'tp-react-web-masked-text';

import { useAuth } from '../../../hooks/AuthContext';
import CustomTextField from '../../CustomTextField';

export const LoginForm = (): JSX.Element => {
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
    <>
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
        >
          Entrar
        </Button>
      </Box>
    </>
  );
};
