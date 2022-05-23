import factory
from factory import alchemy

from database.db import db_session
from models.address import Address
from models.delivery import Delivery
from models.deliveryboy import DeliveryBoy
from models.employee import Employee
from models.user import User

class UserFactory(alchemy.SQLAlchemyModelFactory):
  class Meta:
    model = User
    sqlalchemy_session = db_session

  name = factory.faker.Faker('name')
  telephone = factory.faker.Faker('phone_number',locale='pt_br')
  password= factory.faker.Faker('password')

class DeliveryBoyFactory(alchemy.SQLAlchemyModelFactory):
  class Meta:
    model = DeliveryBoy
    sqlalchemy_session = db_session
  user = factory.SubFactory(UserFactory)
class EmployeeFactory(alchemy.SQLAlchemyModelFactory):
  class Meta:
    model = Employee
    sqlalchemy_session = db_session
  shop = factory.faker.Faker('company',locale='pt-br')
  user = factory.SubFactory(UserFactory)

class AddressFactory(alchemy.SQLAlchemyModelFactory):
  class Meta:
    model = Address
    sqlalchemy_session = db_session

  number = factory.faker.Faker('building_number',locale='pt-br')
  st_or_av = factory.faker.Faker('street_name',locale='pt-br')
  district = factory.faker.Faker('text')

class DeliveryFactory(alchemy.SQLAlchemyModelFactory):
  class Meta:
    model = Delivery
    sqlalchemy_session = db_session

  address = factory.SubFactory(AddressFactory)
  shop = factory.faker.Faker('company',locale='pt-br')
  name = factory.faker.Faker('name')
  telephone = factory.faker.Faker('phone_number',locale='pt_br')
  status = 0


