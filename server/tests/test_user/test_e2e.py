from flask.testing import FlaskClient

from tests.factories import UserFactory

def test_create_user(client: FlaskClient, db_session):
  response = client.post('/register',json={'name':'test','telephone': '7981549327','password': 'testing'})
  assert response.status_code == 201

def test_not_create_user(client: FlaskClient):
  u = UserFactory.create()
  response = client.post('/register',json={'name':u.name,'telephone': u.telephone,'password': u.password})
  assert response.status_code == 400

def test_get_all_users(client: FlaskClient, login: str, db_session):
  response = client.get('/user',headers={'Authorization':'Bearer {}'.format(login)})
  assert response.status_code == 200

def test_not_get_all_users(client: FlaskClient):
  response = client.get('/user')
  assert response.get_json() == {'message': 'A valid token is missing'}

def test_not_get_all_users_with_invalid_token(client: FlaskClient):
  response = client.get('/user',headers={'Authorization':'Bearer {}'.format('1234qwe')})
  assert response.get_json() == {'error': 'the token is invalid'}
