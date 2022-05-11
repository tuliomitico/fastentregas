import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as saut

from .user import User
from database.db import Base, db_session

class DeliveryBoy(Base):
  __tablename__ = 'delivery_boy'
  id = sa.Column(sa.Integer,primary_key=True,autoincrement=True)
  user = orm.relationship('User')
  user_id = sa.Column(saut.UUIDType(binary=False),sa.ForeignKey('user.id',ondelete='CASCADE'))

  def __init__(self,user,*args, **kwargs) -> None:
      super().__init__(*args, **kwargs)
      self.user = user

  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
