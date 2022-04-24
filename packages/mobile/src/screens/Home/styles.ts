import styled from 'styled-components/native';

export const Container = styled.View`
  flex: 1;
  background-color: ${({ theme }) => theme.COLORS.PRIMARY};
  align-items: center;
  justify-content: center;
  padding: 0 16px;
`;

export const HomeText = styled.Text`
  font-weight: bold;
  font-size: 72px;
  color: #f00;
`;
