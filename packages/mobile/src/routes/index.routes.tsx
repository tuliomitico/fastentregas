import React, { ReactNode } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import PublicRoutes from './public/index.routes';
import PrivateRoutes from './private/index.routes';
import { useAuth } from '../hooks/auth';

export default function Routes(
  { children }: { children?: ReactNode },
  ...rest
) {
  const { token } = useAuth();
  return (
    <NavigationContainer {...rest}>
      {token ? <PrivateRoutes /> : <PublicRoutes />}
    </NavigationContainer>
  );
}
