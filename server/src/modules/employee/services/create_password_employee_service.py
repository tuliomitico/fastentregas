import re
from passlib.hash import bcrypt

from database.db import db_session
from models.employee import Employee
from models.user import User

class CreatePasswordEmployeeService():
  def execute(self, telephone: str, password: str):
    formatted_telephone = re.sub(r'\s+',"",telephone)
    user = User.query.filter_by(telephone=formatted_telephone).first()
    if user:
      if user.password:
        raise Exception('Password already created.')
      user.password = bcrypt.using(rounds=10).hash(password)
      db_session.commit()
      employee = Employee.query.filter_by(user_id = user.id).first()
      return employee
    raise Exception('No user found with this phone number')
