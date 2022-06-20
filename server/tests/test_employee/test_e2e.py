import factory
from flask.testing import FlaskClient

from tests.factories import UserFactory

def test_create_employee(client: FlaskClient, login: str):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/employee',json={**db,'shop': 'Loja 0'},headers={'Authorization': f'Bearer {login}'})
  assert res.status_code == 201

def test_create_password_employee(client: FlaskClient, login: str):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/employee',json={**db,'shop':'Loja 0'},headers={'Authorization':f'Bearer {login}'})
  res1 = client.post('/employee/create_password',json=dict(password='test',telephone=db['telephone']))
  assert res1.status_code == 201
  assert res1.json['data'] != {}
