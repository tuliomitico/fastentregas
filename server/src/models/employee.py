import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as saut

from database.db import Base, db_session
from .user import User

class Employee(Base):
  __tablename__ = 'employee'
  id = sa.Column(sa.Integer,primary_key=True)
  user = orm.relationship('User')
  user_id = sa.Column(saut.UUIDType(binary=False),sa.ForeignKey('user.id',ondelete='CASCADE'))
  shop = sa.Column(sa.Text)

  def __init__(self, *args, **kwargs) -> None:
      super().__init__(*args, **kwargs)

  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
