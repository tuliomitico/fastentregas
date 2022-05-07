import { Input } from '@rneui/themed';
import styled from 'styled-components/native';

export const Container = styled.View`
  margin-top: 20px;
`;

export const BaseInput = styled(Input).attrs(() => ({
  labelStyle: {
    color: '#ba3240',
  },
}))`
  border-radius: 20px;
`;
