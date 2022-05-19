import React from 'react';
import { GestureResponderEvent, Text } from 'react-native';
import { Icon, ListItem } from '@rneui/base';
import { DeliveryDataProps } from '../../screens/Deliver/General';

type ItemsProps = {
  expanded: boolean;
  item: DeliveryDataProps;
  onPress: (event: GestureResponderEvent) => void;
};

export default function Item({ item, onPress, expanded }: ItemsProps) {
  return (
    <ListItem.Accordion
      content={
        <>
          <Icon name="place" size={30} />
          <ListItem.Content>
            <ListItem.Title>
              {item.shop} - {item.address.district}
            </ListItem.Title>
          </ListItem.Content>
        </>
      }
      isExpanded={expanded}
      onPress={onPress}
    >
      <ListItem bottomDivider>
        <ListItem.Content>
          <ListItem.Title>{item.id}</ListItem.Title>
          <ListItem.Subtitle>{item.hour}</ListItem.Subtitle>
          <ListItem.Subtitle>{item.address.st_or_av}</ListItem.Subtitle>
          <ListItem.Subtitle>{item.address.number}</ListItem.Subtitle>
        </ListItem.Content>
        <ListItem.Chevron />
      </ListItem>
    </ListItem.Accordion>
  );
}
