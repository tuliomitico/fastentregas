import { Button } from '@rneui/base';
import styled from 'styled-components/native';

export const Container = styled.View`
  background-color: ${({ theme }) => theme.COLORS.PRIMARY};
  padding: 16px 16px;
  height: 100%;
`;

export const HomeText = styled.Text`
  align-self: center;
  font-weight: bold;
  font-size: 32px;
  color: #f00;
`;

export const LoginButton = styled(Button)``;
