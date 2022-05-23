from http import HTTPStatus
from modules.deliveryboy.services.get_delivery_boys_service import GetDeliveryBoysService

from schemas.delivery_boy_schema import DeliveryBoySchema

class GetDeliveryBoysController():
  def handle(self,id):
    delivery_boy = GetDeliveryBoysService().execute(id)
    return DeliveryBoySchema().dump(delivery_boy), HTTPStatus.OK
