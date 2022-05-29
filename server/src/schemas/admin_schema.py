from marshmallow_sqlalchemy import fields
from schemas.user_schema import UserSchema

from .schemas import ma
from models.admin import Admin

class AdminSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Admin
    include_fk = True

  user = fields.Nested(UserSchema)
