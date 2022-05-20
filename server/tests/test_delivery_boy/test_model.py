from sqlalchemy.orm import Session

from models.address import Address
from models.delivery import Delivery
from models.deliveryboy import DeliveryBoy
from models.user import User
from tests.factories import DeliveryBoyFactory

def test_create_delivery_boy(db_session):
  u = User('Teste','00123456789',password='Teste').create()
  d = DeliveryBoy(user=u)
  assert [d.create()] == DeliveryBoy.query.all()

def test_create_delivery_boy_linking(db_session: Session):
  user = User('Teste','00123456789',password='Teste').create()
  address = Address('Teste','Rua Teste',123)
  delivery = Delivery('0012345678','Teste','LojaTeste',0,address=address)
  delivery_boy = DeliveryBoy(user=user)
  delivery_boy.deliverys.append(delivery)
  db_session.add(user)
  db_session.add(address)
  db_session.add(delivery)
  db_session.add(delivery_boy)
  db_session.commit()
  assert delivery_boy.deliverys[0].id == delivery.id


def test_factory():
  delivery_boy = DeliveryBoyFactory.build_batch(10)
  assert len(delivery_boy) == 10

def test_factory_does_not_affect_database(db_session):
  DeliveryBoyFactory.create()
  assert DeliveryBoy.query.count() == 0
