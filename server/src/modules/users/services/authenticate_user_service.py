from models.user import User


class AuthenticateUserService():
  def execute(self,telephone: str, password: str):
    users = User.query.filter(telephone==telephone).first()
    return users
