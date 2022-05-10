import React from 'react';
import { Icon } from '@rneui/base';
import * as Yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';
import { useForm } from 'react-hook-form';
import { MaskService } from 'react-native-masked-text';

import Input from '../../../components/Input';
import { Container, HomeText, LoginButton } from './styles';
import { SignInCredentials, useAuth } from '../../../hooks/auth';

const Home: React.FC = () => {
  const { signIn } = useAuth();
  const schema = Yup.object().shape({
    telephone: Yup.string()
      .required('Telefone obrigatório')
      .min(11, 'Telefone não válido'),
    password: Yup.string()
      .required('Senha obrigatória')
      .min(3, 'A senha deve ser maior que 8 dígitos'),
  });
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({
    resolver: yupResolver(schema),
    mode: 'onBlur',
    defaultValues: {
      telephone: '',
      password: '',
    },
  });
  const handleLogin = async (data: SignInCredentials): Promise<void> => {
    const { telephone: maskedTelephone, password } = data;
    const telephone = MaskService.toRawValue('cel-phone', maskedTelephone);
    console.log(telephone);

    await signIn({
      telephone,
      password,
    });
  };
  return (
    <Container>
      <HomeText>Fast Entregas</HomeText>
      <Input
        errors={errors}
        control={control}
        name="telephone"
        label="Telefone"
        inputMask
        type={'cel-phone'}
        options={{
          maskType: 'BRL',
          withDDD: true,
          dddMask: '(99) ',
        }}
        autoCapitalize="none"
        keyboardType="phone-pad"
        leftIcon={<Icon name="person" size={24} color="white" />}
        color="purple"
      />
      <Input
        errors={errors}
        control={control}
        name="password"
        label="Senha"
        leftIcon={<Icon name="lock" size={24} color="white" />}
        autoCapitalize="none"
        secureTextEntry
        color="purple"
      />
      <LoginButton title={'Entrar'} onPress={handleSubmit(handleLogin)} />
    </Container>
  );
};

export default Home;
