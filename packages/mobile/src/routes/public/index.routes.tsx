import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import Home from '../../screens/onboarding/Home';
import Register from '../../screens/onboarding/Register';

const Stack = createStackNavigator();

export default function Public() {
  return (
    <Stack.Navigator initialRouteName="Home">
      <Stack.Screen
        name="Register"
        component={Register}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="Home"
        component={Home}
        options={{ headerShown: false }}
      />
    </Stack.Navigator>
  );
}
