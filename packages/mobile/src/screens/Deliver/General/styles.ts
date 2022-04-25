import styled from 'styled-components/native';

export const Container = styled.View`
  background-color: ${({ theme }) => theme.COLORS.PRIMARY};
  padding: 0 16px;
  justify-content: center;
  align-items: center;
  height: 100%;
`;

export const GeneralText = styled.Text`
  color: ${({ theme }) => theme.COLORS.SECONDARY};
`;
