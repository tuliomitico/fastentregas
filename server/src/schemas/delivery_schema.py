from marshmallow import fields
from marshmallow_enum import EnumField

from models.delivery import Delivery, StatusType
from .schemas import ma

class DeliverySchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Delivery

  id = ma.auto_field(dump_only=True)
  name = ma.auto_field()
  telephone = ma.auto_field()
  hour = fields.DateTime(format="%H:%M:%S",dump_only=True)
  shop = ma.auto_field()
  status = EnumField(StatusType)
