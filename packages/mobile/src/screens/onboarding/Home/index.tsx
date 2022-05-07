import { Icon } from '@rneui/base';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { useForm } from 'react-hook-form';
import Input from '../../../components/Input';

import { Container, HomeText } from './styles';

const Home: React.FC = () => {
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm({});
  return (
    <Container>
      <HomeText>Fast Entregas</HomeText>
      <Input
        errors={errors}
        control={control}
        name="telephone"
        label="Telefone"
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
      <StatusBar style="auto" />
    </Container>
  );
};

export default Home;
