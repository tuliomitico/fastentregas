from models.user import User

from tests.factories import UserFactory

def test_create_user(db_session):
  u = User('test','0012345678',password='testing')
  assert [u.create()] == User.query.all()

def test_create_user_without_password(db_session):
  u = User('test','0012345678').create()
  assert User.query.get(u.id).password == None

def test_factory():
  user = UserFactory.build_batch(10)
  assert len(user) == 10

def test_user_factory_without_password(db_session):
  user = UserFactory(password=None).create()
  assert user.password == None

def test_user_factory_not_affects_database(db_session):
  UserFactory.create()
  assert User.query.count() == 0
