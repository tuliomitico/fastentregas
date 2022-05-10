from http import HTTPStatus

from flask import request, jsonify

from schemas.user_schema import UserSchema
from modules.users.services.create_user_service import CreateUserService

class CreateUserController():
  def handle(self):
    data = request.get_json()
    try:
      user = CreateUserService().execute(data['name'],data['telephone'],data['password'])
    except Exception as e:
      return jsonify(error=str(e)), HTTPStatus.BAD_REQUEST
    user_schema=UserSchema(load_instance=True)
    return jsonify(data=user_schema.dump(user)), HTTPStatus.CREATED
