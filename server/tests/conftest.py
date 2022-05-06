from datetime import datetime, timedelta
from flask import Flask
import jwt

import pytest
from src.server import create_app

@pytest.fixture
def app():
  app = create_app('src.config.TestingConfig')
  yield app

@pytest.fixture
def client(app: Flask):
  return app.test_client()

@pytest.fixture
def login(app: Flask):
  return jwt.encode({
    'sub':'test',
    'iat': datetime.utcnow(),
    'exp': datetime.utcnow() + timedelta(minutes=1)
    },
    app.config.get('SECRET_KEY'),
    algorithm='HS256'
  )
