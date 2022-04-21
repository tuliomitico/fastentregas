import { StatusBar } from 'expo-status-bar';
import React from 'react';

import { Container, HomeText } from './styles';

const Home: React.FC = () => {
  return (
    <Container>
      <HomeText>Fast Entregas</HomeText>
      <StatusBar style="auto" />
    </Container>
  );
};

export default Home;
