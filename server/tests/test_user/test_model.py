from models.user import User

from tests.factories import UserFactory

def test_create_user(db_session):
  u = User('test','0012345678',password='testing')
  assert [u.create()] == User.query.all()

def test_factory():
  user = UserFactory.build_batch(10)
  assert len(user) == 10
