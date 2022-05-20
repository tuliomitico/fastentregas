import pytest

from modules.users.services.create_user_service import CreateUserService
from tests.factories import UserFactory

def test_user_already_exists_error(db_session):
  u = UserFactory(name='Mary Test',telephone='7180101787',password='test').create()
  with pytest.raises(Exception):
    assert CreateUserService().execute(u.name,u.telephone,u.password) == u

def test_user_without_password(db_session):
  with pytest.raises(Exception):
    user = CreateUserService().execute('test','0012345678',None)
    assert type(user) == type(UserFactory._meta.model)
