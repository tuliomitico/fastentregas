from datetime import datetime, timedelta
from flask import Flask
import jwt

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import  scoped_session, sessionmaker
from src.server import create_app
from database.db import Base, init_db, db_session as Session

from tests.test_user.test_model import UserFactory

engine = create_engine('sqlite:///database.sqlite3', echo=True)
TestingLocalSession = scoped_session(sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
))

@pytest.fixture
def app():
  app = create_app('src.config.TestingConfig')
  yield app

@pytest.fixture(scope="function") # or "module" (to teardown at a module level)
def db_session(app: Flask):
  Session.remove()
  init_db(engine)
  yield
  Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope='function')
def isolated_session(app: Flask):
  Base.metadata.create_all(bind=engine)
  Base.query = TestingLocalSession.query_property()
  session = TestingLocalSession()
  yield session
  session.close()
  Base.metadata.drop_all(bind=engine)

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
