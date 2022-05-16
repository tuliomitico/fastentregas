import React, { useState, useEffect } from 'react';
import { ListRenderItem } from 'react-native';
// import { ListItem } from '@rneui/base';
// import Icon from 'react-native-vector-icons/MaterialIcons';

import api from '@fastentregas/axios-config';
import { Container, GeneralText } from './styles';
import { FlatList } from 'react-native-gesture-handler';
import Item from '../../../components/Item';

type AddressDataProps = {
  district: string;
  st_or_av: string; // street or avenue
  number: number;
};

export type DeliveryDataProps = {
  id: string;
  hour: string;
  address: AddressDataProps;
};

type DeliveryData = {
  deliverys: DeliveryDataProps[];
};

const General: React.FC = () => {
  const [data, setData] = useState([] as DeliveryDataProps[]);
  const [selectedItems, setSelectedItems] = useState<string[]>([]);
  const handleOnPress = item => {
    if (selectedItems.length) {
      return selectItems(item.id);
    }

    // here you can add you code what do you want if user just do single tap
    console.log('pressed');
  };

  const getSelected = (item: DeliveryDataProps) =>
    selectedItems.includes(item.id);

  const selectItems = (id: string) => {
    if (selectedItems.includes(id)) {
      const newListItems = selectedItems.filter(listItem => listItem !== id);
      return setSelectedItems([...newListItems]);
    }
    setSelectedItems([...selectedItems, id]);
  };

  useEffect(() => {
    api
      .get<DeliveryData>('/deliver')
      .then(response => response.data)
      .then(data => setData(data.deliverys));
  }, []);

  const renderItems: ListRenderItem<DeliveryDataProps> = ({ item }) => {
    return (
      <Item
        item={item}
        expanded={getSelected(item)}
        onPress={() => {
          handleOnPress(item);
          selectItems(item.id);
          console.log(selectedItems);
        }}
      />
    );
  };

  return (
    <Container>
      <GeneralText>Entregas recentes</GeneralText>

      <FlatList
        data={data}
        keyExtractor={item => item.id}
        renderItem={renderItems}
        style={{ height: 300 }}
        contentContainerStyle={{
          paddingBottom: 50,
          justifyContent: 'center',
        }}
      />
    </Container>
  );
};

export default General;
