from functools import wraps

from flask import request, current_app, g
import jwt

from models.user import User

class Auth():
  def login_required(self,f):
    @wraps(f)
    def decorator(*args,**kwargs):
      authorization = None
      if 'Authorization' in request.headers:
        authorization = request.headers.get('Authorization','').split()
      if not authorization:
        return {'message': 'A valid token is missing'}, 403
      if len(authorization) == 2:
        try:
          token = authorization[1]
          data = jwt.decode(
            token,
            current_app.config.get('SECRET_KEY'),
            algorithms=['HS256']
          )
          user_exists = User.query.filter_by(name=data['sub']).first()

          if user_exists:
            g.user = user_exists.name
        except:
          return {'error': 'the token is invalid'}, 403
        return f(*args,**kwargs)
      return decorator

  def current_user(self):
    if hasattr(g,'user'):
      return g.user
