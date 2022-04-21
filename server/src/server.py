import typing as t

from flask import Flask

def index():
  return {"Hello":"World"}, 200

def create_app(config: t.Union[str,t.Dict[str,str],None] = None) -> Flask:
  app = Flask(__name__)
  if isinstance(config,dict):
    app.config.update(config)
  app.add_url_rule('/','index',index)
  return app
