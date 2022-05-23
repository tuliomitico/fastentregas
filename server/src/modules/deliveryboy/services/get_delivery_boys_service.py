from models.deliveryboy import DeliveryBoy

class GetDeliveryBoysService():
  def execute(self, id: int) :
    return  DeliveryBoy.query.get(id)
