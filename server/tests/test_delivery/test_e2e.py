from flask.testing import FlaskClient

def test_get_all_deliverys(client: FlaskClient, db_session):
  response = client.get('/deliver')
  assert response.status_code == 200

def test_create_delivery(client: FlaskClient, db_session):
  res = client.post('/deliver',json={
    'district': 'Santa Efigenia',
    'st_or_av': 'Rua dos Bobos',
    'number': 0,
    'shop': 'Loja 0',
    'telephone': '00 1234 5678',
    'status': 'avaliable',
    'name': 'Zé Ninguém'
  })
  assert res.status_code == 201
