from models.deliveryboy import DeliveryBoy

class GetDeliveryBoyService():
  def execute(self):
    delivery_boy = DeliveryBoy.query.all()
    return delivery_boy
