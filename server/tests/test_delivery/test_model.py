from models.address import Address
from models.delivery import Delivery
from tests.factories import DeliveryFactory

def test_create_delivery(db_session):
  a = Address('Santa Mae de Deus','Rua dos Bobos',321).create()
  d = Delivery('00 1234 5678','Beltrano','Loja 0',0,address=a).create()
  assert [d] == Delivery.query.all()

def test_factory():
  d = DeliveryFactory.build_batch(10)
  assert len(d) == 10

def test_factory_does_not_affect_database(db_session):
  DeliveryFactory.create()
  assert Delivery.query.count() == 0
