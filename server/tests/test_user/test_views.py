from flask import url_for
from flask.ctx import RequestContext
from flask.testing import FlaskClient

def test_url_route(
  test_request: RequestContext,
  client: FlaskClient,
  login: str,
  db_session
):
  res = client.get(url_for('index.get_users'),headers={'Authorization': f'Bearer {login}'})
  assert res.status_code == 200
