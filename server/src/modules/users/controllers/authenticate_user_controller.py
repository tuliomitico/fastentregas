from datetime import datetime, timedelta
from http import HTTPStatus

from flask import current_app, request, jsonify
import jwt

from modules.users.services.authenticate_user_service import (
  AuthenticateUserService
)
class AuthenticateUserController():
  def handle(self):
    data = request.get_json()
    try:
      user = AuthenticateUserService().execute(
        telephone = data['telephone'],
        password = data['password']
      )
      token = jwt.encode({
        "sub": user.name,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(minutes=45)
      },
      current_app.config.get('SECRET_KEY'),
      algorithm='HS256')
      return { "token": token }, HTTPStatus.OK
    except Exception as e:
      return jsonify({"error": str(e)}), HTTPStatus.UNAUTHORIZED
