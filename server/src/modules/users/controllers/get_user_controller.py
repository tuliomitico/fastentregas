from http import HTTPStatus

from modules.users.services.get_user_service import GetUserService
from schemas.user_schema import UserSchema

class GetUserController():
  def handle(self):
    users = GetUserService().execute()
    users_schema = UserSchema(many=True)
    return { "users" : users_schema.dump(users)}, HTTPStatus.OK
