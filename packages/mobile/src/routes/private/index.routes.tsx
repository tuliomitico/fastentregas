import React from 'react';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';
import General from '../../screens/Deliver/General';
import Paths from '../../screens/Deliver/Paths';
import { Header, Avatar } from '@rneui/base';
import { SafeAreaView, Text } from 'react-native';

const DeliverTab = createMaterialTopTabNavigator();

export default function IndexRouter() {
  return (
    <SafeAreaView style={{ height: '100%' }}>
      <Header
        barStyle="dark-content"
        centerComponent={
          <Text style={{ color: '#fff' }}>Maicão {'"Cabiçulinha"'} Brito</Text>
        }
        rightComponent={
          <Avatar
            source={{ uri: 'https://www.github.com/maykbrito.png' }}
            size="medium"
            rounded
          />
        }
        placement="right"
      />
      <DeliverTab.Navigator initialRouteName="Entregas disponivéis">
        <DeliverTab.Screen component={General} name="Entregas disponivéis" />
        <DeliverTab.Screen component={Paths} name="Minhas rotas" />
      </DeliverTab.Navigator>
    </SafeAreaView>
  );
}
