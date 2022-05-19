import { Button } from '@rneui/themed';
import styled from 'styled-components/native';

export const Container = styled.View`
  background-color: ${({ theme }) => theme.COLORS.PRIMARY};
  padding: 16px 16px;
  height: 100%;
`;

export const SignupButton = styled(Button).attrs(() => ({
  buttonStyle: {
    backgroundColor: '#01b0f1',
  },
}))``;
