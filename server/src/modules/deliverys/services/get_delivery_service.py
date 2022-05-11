from models.delivery import Delivery


class GetDeliveryService():
  def execute(self):
    deliverys = Delivery.query.all()
    return deliverys
