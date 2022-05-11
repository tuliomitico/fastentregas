from models.delivery import Delivery
from schemas.delivery_schema import DeliverySchema

class CreateDeliveryService():
  def execute(self, name: str, shop: str, telephone: str, status: str):
    delivery_schema = DeliverySchema().load(dict(name=name,shop=shop,telephone=telephone,status=status))
    delivery = Delivery(**delivery_schema).create()
    return delivery
