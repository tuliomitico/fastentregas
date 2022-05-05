from marshmallow import fields

from .schemas import ma
from models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User

  password = fields.Str(load_only = True)
