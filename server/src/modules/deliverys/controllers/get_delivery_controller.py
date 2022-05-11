from http import HTTPStatus
from schemas.delivery_schema import DeliverySchema

from modules.deliverys.services.get_delivery_service import GetDeliveryService

class GetDeliveryController():
  def handle(self):
    deliverys = GetDeliveryService().execute()
    deliverys_schema = DeliverySchema(many=True)
    return {"deliverys": deliverys_schema.dump(deliverys)}, HTTPStatus.OK
