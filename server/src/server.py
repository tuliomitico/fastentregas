import typing as t

from flask import Flask

from .routes import blp, blp_auth, blp_delivery
from .schemas.schemas import ma
from .database.db import db_session, init_db

def setup_app(app: Flask) -> None:
  @app.teardown_appcontext
  def shutdown_session(exception=None):
    db_session.remove()
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
