from factory import alchemy
import factory
from models.user import User
from database.db import db_session

class UserFactory(alchemy.SQLAlchemyModelFactory):
  class Meta:
    model = User
    sqlalchemy_session = db_session

  name = factory.faker.Faker('name')
  telephone = factory.faker.Faker('phone_number',locale='pt_br')
  password= factory.faker.Faker('password')
