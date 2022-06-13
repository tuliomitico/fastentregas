import React, { useEffect, useState } from 'react';
import { ScrollView } from 'react-native';

import { Container } from './styles';
import Item from '../../../components/Item';
import DeliverService from '../../../services/DeliverService';

const Paths: React.FC = () => {
  const [data, setData] = useState([]);

  const getDeliveryList = async () => {
    const delivery = await DeliverService.closedDelivery();
    setData(delivery.deliverys);
  };

  useEffect(() => {
    getDeliveryList();
  }, []);

  return (
    <Container>
      <ScrollView>
        {data.map(item => (
          <Item key={item.id} item={item} />
        ))}
      </ScrollView>
    </Container>
  );
};

export default Paths;
