import typing as t

from flask import Flask

from .routes import blp

def setup_app(app: Flask) -> None:
  return

def create_app(config: t.Union[str,t.Dict[str,str],None] = None) -> Flask:
  app = Flask(__name__)
  if isinstance(config,dict):
    app.config.update(config)
  app.config.from_object(config)
  app.register_blueprint(blp)
  return app
