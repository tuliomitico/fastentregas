from marshmallow import fields

from models.address import Address
from .schemas import ma

class AddressSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Address

  id = fields.Integer(load_only=True)
