from passlib.hash import bcrypt

from models.admin import Admin
from models.employee import Employee
from models.deliveryboy import DeliveryBoy
from models.user import User

class AuthenticateUserService():
  def execute(self,telephone: str, password: str):
    formatted_telephone = telephone.strip()
    user = User.query.filter_by(telephone=formatted_telephone).first()
    if not user:
      raise Exception('Usuario não cadastrado')
    is_valid_password = bcrypt.verify(password, user.password)
    if not is_valid_password:
      raise Exception('Senha inválida')
    admin = Admin.query.filter_by(user_id = user.id).first()
    if admin:
      return { "user": admin, "role": 3 }
    employee = Employee.query.filter_by(user_id = user.id).one_or_none()
    if employee:
      return { "user": employee, "role": 2 }
    delivery_boy = DeliveryBoy.query.filter_by(user_id = user.id).one_or_none()
    if delivery_boy:
      return { "user": delivery_boy, "role": 1 }
