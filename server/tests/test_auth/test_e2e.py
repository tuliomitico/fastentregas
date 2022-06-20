import factory
from flask.testing import FlaskClient

from tests.factories import UserFactory
from models.employee import Employee

def test_authenticate_user(client: FlaskClient,db_session):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/register',json=db)
  Employee(user_id=res.json['data']['id']).create()
  res1 = client.post('/login',json={'telephone':db['telephone'],'password':db['password']})
  assert res1.status_code == 200

def test_not_authenticate_user(client: FlaskClient,db_session):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/login',json={'telephone':db['telephone'],'password':db['password']})
  assert res.status_code == 401

def test_not_authenticate_user_by_wrong_password(client: FlaskClient,db_session):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/register',json=db)
  res1 = client.post('/login',json={'telephone':db['telephone'],'password':'test'})
  assert res1.status_code == 401
