import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as saut

from database.db import Base, db_session

class DeliveryBoy(Base):
  __tablename__ = 'delivery_boy'
  id = sa.Column(sa.BigInteger,primary_key=True,autoincrement=True)
  user = orm.relationship('User')
  user_id = sa.Column(saut.UUIDType(binary=False))

  def __init__(self, user_id: str,*args, **kwargs) -> None:
      super().__init__(*args, **kwargs)
      self.user_id = user_id

  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
