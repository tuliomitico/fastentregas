from http import HTTPStatus

from middlewares.auth import auth
from modules.deliveryboy.services.delete_delivery_of_delivery_boy_service import DeleteDeliveryOfDeliveryBoyService

class DeleteDeliveryOfDeliveryBoyController():
  def handle(self, pk: int):
    DeleteDeliveryOfDeliveryBoyService().execute(pk = pk,name = auth.current_user())
    return '', HTTPStatus.NO_CONTENT
