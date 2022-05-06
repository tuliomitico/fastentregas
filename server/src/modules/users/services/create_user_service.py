from passlib.hash import bcrypt

from models.user import User

class CreateUserService():
  def execute(self,telephone: str, password: str):
    formatted_telephone = telephone.strip()
    user_already_exists = User.query.filter_by(telephone=formatted_telephone).first()
    if user_already_exists:
      raise Exception("User already exists")
    elif password is None:
      raise Exception("Please, provide a password")
    encrypted_password = bcrypt.using(rounds=10).hash(password)
    user = User(telephone=formatted_telephone,password=encrypted_password).create()
    return user
