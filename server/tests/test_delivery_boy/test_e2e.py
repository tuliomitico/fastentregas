import factory
from flask.testing import FlaskClient

from tests.factories import UserFactory

def test_create_delivery_boy(client: FlaskClient, db_session):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  res = client.post('/register/delivery_boy',json=db)
  assert res.status_code == 201

def test_create_password_delivery_boy(client: FlaskClient, db_session):
  db = factory.build(
    dict,
    FACTORY_CLASS = UserFactory
  )
  db.pop('password',None)
  res = client.post('/register/delivery_boy',json=db)
  res1 = client.post('/delivery_boy/create_password',json=dict(password='test',telephone=db['telephone']))
  assert res1.status_code == 201
