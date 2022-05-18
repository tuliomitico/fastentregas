from models.delivery import Delivery
from schemas.address_schema import AddressSchema
from schemas.delivery_schema import DeliverySchema

class CreateDeliveryService():
  def execute(
    self,
    name: str,
    shop: str,
    telephone: str,
    status: str,
    district: str,
    st_or_av: str,
    number: int
  ):
    address_schema = AddressSchema(load_instance=True)
    delivery_schema = DeliverySchema().load(dict(
      name = name,
      shop = shop,
      telephone = telephone,
      status = status
    ))
    delivery = Delivery(
      address=address_schema.load(
        dict(st_or_av = st_or_av, district = district, number = number)),
        **delivery_schema).create()
    return delivery
