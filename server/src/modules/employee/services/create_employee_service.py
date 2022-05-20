import re

from models.user import User
from models.employee import Employee

class CreateEmployeeService():
  def execute(self, name: str, telephone: str, shop: str):
    formatted_telephone = re.sub(r'\s+',"",telephone) # Remove white spaces
    user_already_exists: User = User.query.filter_by(telephone = formatted_telephone).first()
    if user_already_exists:
      employee_already_exists = Employee.query.filter_by(user_id = user_already_exists.id).first()
      if employee_already_exists:
        raise Exception('Employee already exists.')
    user = User(name=name,telephone=telephone)
    employee = Employee(user=user,shop=shop).create()
    return employee
