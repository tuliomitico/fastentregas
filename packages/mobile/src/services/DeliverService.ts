import api from '@fastentregas/axios-config';

export default class DeliverService {
  static async openDelivery(): Promise<any> {
    const { data } = await api.get('/deliver');
    return data;
  }

  static async closedDelivery(): Promise<any> {
    const { data } = await api.get('/delivery_boy/deliver');
    return data;
  }
}
