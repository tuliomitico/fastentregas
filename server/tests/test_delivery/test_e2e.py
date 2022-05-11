from flask.testing import FlaskClient

def test_get_all_deliverys(client: FlaskClient, db_session):
  response = client.get('/deliver')
  assert response.status_code == 200
