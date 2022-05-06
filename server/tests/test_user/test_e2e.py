from flask.testing import FlaskClient

def test_get_all_users(client: FlaskClient, login: str):
  response = client.get('/user',headers={'Authorization':'Bearer {}'.format(login)})
  assert response.status_code == 200

def test_not_get_all_users(client: FlaskClient):
  response = client.get('/user')
  assert response.get_json() == {'message': 'A valid token is missing'}

def test_not_get_all_users_with_invalid_token(client: FlaskClient):
  response = client.get('/user',headers={'Authorization':'Bearer {}'.format('1234qwe')})
  assert response.get_json() == {'error': 'the token is invalid'}
