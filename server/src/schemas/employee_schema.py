from marshmallow_sqlalchemy import fields
from schemas.user_schema import UserSchema

from .schemas import ma
from models.employee import Employee

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
  class Meta:
    model = Employee
    include_fk = True

  user = fields.Nested(UserSchema)
