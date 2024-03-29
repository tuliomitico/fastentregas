import typing as t

from flask import Flask

from .cors import cors
from .database.db import db_session
from .middlewares.jwt import jwt
from .routes import blp, blp_auth, blp_delivery
from .schemas.schemas import ma

def setup_app(app: Flask) -> None:
  @app.teardown_appcontext
  def shutdown_session(exception=None):
    db_session.remove()
  jwt.init_app(app)
  cors.init_app(app, resources=r'/*')
  ma.init_app(app)

def create_app(config: t.Union[str,t.Dict[str,str],None] = None) -> Flask:
  app = Flask(__name__)
  if isinstance(config,dict):
    app.config.update(config)
  app.config.from_object(config)
  setup_app(app)
  app.register_blueprint(blp)
  app.register_blueprint(blp_auth)
  app.register_blueprint(blp_delivery)
  return app
