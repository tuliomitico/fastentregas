import { StatusBar } from 'expo-status-bar';
import React from 'react';
import Input from '../../../components/Input';

import { Container, HomeText } from './styles';

const Home: React.FC = () => {
  return (
    <Container>
      <HomeText>Fast Entregas</HomeText>
      <Input name="telephone" />
      <Input name="password" />
      <StatusBar style="auto" />
    </Container>
  );
};

export default Home;
