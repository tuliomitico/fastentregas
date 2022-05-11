from marshmallow_sqlalchemy import fields
from schemas.user_schema import UserSchema

from .schemas import ma
from models.deliveryboy import DeliveryBoy

class DeliveryBoySchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = DeliveryBoy
    include_fk = True

  user = fields.Nested(UserSchema)
