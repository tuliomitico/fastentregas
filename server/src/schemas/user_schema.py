from .schemas import ma
from models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = User
