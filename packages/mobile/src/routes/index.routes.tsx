import React, { ReactNode } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import PublicRoutes from './public/index.routes';
import PrivateRoutes from './private/index.routes';

export default function Routes(
  { children }: { children?: ReactNode },
  ...rest
) {
  return (
    <NavigationContainer {...rest}>
      <PrivateRoutes />
    </NavigationContainer>
  );
}
