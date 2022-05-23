import factory
from flask.testing import FlaskClient

from tests.factories import UserFactory

def test_create_employee(client: FlaskClient, db_session):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/employee',json={**db,'shop': 'Loja 0'})
  assert res.status_code == 201

def test_create_password_employee(client: FlaskClient, db_session):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/employee',json={**db,'shop':'Loja 0'})
  res1 = client.post('/employee/create_password',json=dict(password='test',telephone=db['telephone']))
  assert res1.status_code == 201
  assert res1.json['data'] != {}
