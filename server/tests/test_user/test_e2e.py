from flask.testing import FlaskClient

def test_get_all_users(client: FlaskClient):
  response = client.get('/user')
  assert response.status_code == 200
