from marshmallow_sqlalchemy import fields

from .schemas import ma
from models.deliveryboy import DeliveryBoy
from schemas.delivery_schema import DeliverySchema
from schemas.user_schema import UserSchema
class DeliveryBoySchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = DeliveryBoy
    include_fk = True

  user = fields.Nested(UserSchema)
  deliverys = fields.Nested(DeliverySchema,many=True)
