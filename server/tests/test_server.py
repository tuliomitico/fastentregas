from flask import Flask
from flask.testing import FlaskClient
from src import __version__


def test_version():
    assert __version__ == '0.1.0'

def test_index_code(client: FlaskClient):
  response = client.get('/')
  assert response.status_code == 200

def test_config_app(app: Flask):
  assert app.config.get('TESTING') is not False
