import React, { useState, useEffect } from 'react';
import { Text } from 'react-native';
import { ListItem } from '@rneui/base';
import Icon from 'react-native-vector-icons/MaterialIcons';

import api from '@fastentregas/axios-config';
import { Container, GeneralText } from './styles';

type DeliveryDataProps = {
  code: string;
  hour: string;
};

type DeliveryData = {
  deliverys: DeliveryDataProps[];
};

const General: React.FC = () => {
  const [data, setData] = useState([] as DeliveryDataProps[]);
  const [expanded, setExpanded] = useState(false);

  useEffect(() => {
    api
      .get<DeliveryData>('/deliver')
      .then(response => response.data)
      .then(data => setData(data.deliverys));
  }, []);

  return (
    <Container>
      <GeneralText>Entregas recentes</GeneralText>
      <ListItem.Accordion
        content={
          <>
            <Icon name="place" size={30} />
            <ListItem.Content>
              <ListItem.Title>
                <Text>Santa Mônica</Text>
              </ListItem.Title>
            </ListItem.Content>
          </>
        }
        isExpanded={expanded}
        onPress={() => setExpanded(!expanded)}
        tvParallaxProperties={undefined}
        hasTVPreferredFocus={undefined}
      >
        {data.map((l, i) => (
          <ListItem
            key={i}
            bottomDivider
            hasTVPreferredFocus={undefined}
            tvParallaxProperties={undefined}
          >
            <ListItem.Content>
              <ListItem.Title>
                <Text style={{ color: '#010' }}>{l.code}</Text>
              </ListItem.Title>
              <ListItem.Subtitle>{l.hour}</ListItem.Subtitle>
            </ListItem.Content>
            <ListItem.Chevron hasTVPreferredFocus={undefined} />
          </ListItem>
        ))}
      </ListItem.Accordion>
    </Container>
  );
};

export default General;
