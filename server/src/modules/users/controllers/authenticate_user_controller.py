from http import HTTPStatus

from flask import request

from schemas.user_schema import UserSchema
from modules.users.services.authenticate_user_service import AuthenticateUserService

class AuthenticateUserController():
  def handle(self):
    data = request.get_json()
    user = AuthenticateUserService().execute(telephone = data['telephone'],password = 'qwe')
    user_schema = UserSchema()
    return { "user": user_schema.dump(user)}, HTTPStatus.OK
