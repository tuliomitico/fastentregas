import React from 'react';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import General from '../../screens/Deliver/General';
import Paths from '../../screens/Deliver/Paths';

const DeliverTab = createMaterialTopTabNavigator();

export default function IndexRouter() {
  return (
    <DeliverTab.Navigator initialRouteName="Entregas disponivéis">
      <DeliverTab.Screen component={General} name="Entregas disponivéis" />
      <DeliverTab.Screen component={Paths} name="Minhas rotas" />
    </DeliverTab.Navigator>
  );
}
