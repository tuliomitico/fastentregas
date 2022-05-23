from http import HTTPStatus

from modules.deliveryboy.services.get_delivery_boy_service import GetDeliveryBoyService
from schemas.delivery_boy_schema import DeliveryBoySchema

class GetDeliveryBoyController():
  def handle(self):
    delivery_boys_schema = DeliveryBoySchema(many=True)
    delivery_boy = GetDeliveryBoyService().execute()
    return {'delivery_boys':delivery_boys_schema.dump(delivery_boy)},HTTPStatus.OK
