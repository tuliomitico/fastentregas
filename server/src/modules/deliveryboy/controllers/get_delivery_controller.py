from http import HTTPStatus

from middlewares.auth import auth
from modules.deliveryboy.services.get_delivery_service import GetDeliveryService
from schemas.delivery_boy_schema import DeliveryBoySchema

class GetDeliveryController():
  def handle(self, pk: int):
    delivery = GetDeliveryService().execute(name=auth.current_user(),pk=pk)
    delivery_boy_schema = DeliveryBoySchema(exclude=['user','user_id','id'])
    result = delivery_boy_schema.dump(delivery)
    return result, HTTPStatus.CREATED
