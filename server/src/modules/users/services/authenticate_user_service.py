from passlib.hash import bcrypt

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
    return user
