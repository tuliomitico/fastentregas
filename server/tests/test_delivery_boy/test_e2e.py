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
