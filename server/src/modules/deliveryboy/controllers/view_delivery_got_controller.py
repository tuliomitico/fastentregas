from http import HTTPStatus

from middlewares.auth import auth
from modules.deliveryboy.services.view_delivery_got_service import ViewDeliveryGotService
from schemas.delivery_boy_schema import DeliveryBoySchema

class ViewDeliveryGotController():
  def handle(self):
    delivery_boy_schema = DeliveryBoySchema(exclude=['user','user_id','id'])
    delivery = ViewDeliveryGotService().execute(name=auth.current_user())
    result = delivery_boy_schema.dump(delivery)
    return result, HTTPStatus.OK
