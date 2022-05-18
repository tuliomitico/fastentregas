from datetime import datetime, timedelta
from flask import Flask
import jwt

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, Connection
from sqlalchemy.orm import  scoped_session, sessionmaker
from src.server import create_app
from database.db import Base, db_session as Session

engine = create_engine('sqlite:///database.sqlite3', echo=True)
TestingLocalSession = scoped_session(sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine
))
@pytest.fixture(scope='session')
def engine_alt():
  return create_engine('sqlite:///database.sqlite3', echo=True)

@pytest.fixture(scope='session')
def tables(engine_alt):
  Base.metadata.create_all(engine_alt)
  yield
  Base.metadata.drop_all(engine_alt)

@pytest.fixture
def db_session(engine_alt: Engine, tables):
  connection = engine_alt.connect()
  transaction = connection.begin()
  Session.remove()
  Session.configure(bind=connection)
  session: scoped_session = Session()
  yield session
  session.close()
  transaction.rollback()
  connection.close()

@pytest.fixture
def test_request(app: Flask):
  ctx = app.test_request_context()
  ctx.push()
  yield ctx
  ctx.pop()

@pytest.fixture
def app():
  app = create_app('src.config.TestingConfig')
  yield app

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
