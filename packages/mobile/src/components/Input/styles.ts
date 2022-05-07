import { Input } from '@rneui/themed';
import styled from 'styled-components/native';

export const Container = styled.View`
  margin-top: 20px;
`;

export const Error = styled.Text`
  font-size: 14px;
  color: 'red';
  padding: 4px 4px 0 4px;
`;

export const BaseInput = styled(Input).attrs(() => ({
  labelStyle: {
    color: 'white',
  },
  containerStyle: {
    color: 'white',
  },
  inputContainerStyle: {
    color: 'white',
  },
  inputStyle: {
    color: 'white',
  },
}))`
  border-radius: 20px;
`;
