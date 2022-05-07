import styled from 'styled-components/native';

export const Container = styled.View`
  background-color: ${({ theme }) => theme.COLORS.PRIMARY};
  padding: 0 16px;
  height: 100%;
`;

export const HomeText = styled.Text`
  font-weight: bold;
  font-size: 32px;
  color: #f00;
`;
