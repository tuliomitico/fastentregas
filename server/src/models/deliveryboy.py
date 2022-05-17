import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as saut

from database.db import Base, db_session
from .delivery import Delivery
from .user import User

delivery_deliveryboy = sa.Table(
  'delivery_deliveryboy',
  Base.metadata,
  sa.Column('deliveryboy_id',sa.Integer,sa.ForeignKey('delivery_boy.id',ondelete='CASCADE')),
  sa.Column('delivery_id',sa.Integer, sa.ForeignKey('delivery.id',ondelete='CASCADE'))
)

class DeliveryBoy(Base):
  __tablename__ = 'delivery_boy'
  id = sa.Column(sa.Integer,primary_key=True,autoincrement=True)
  user = orm.relationship('User')
  user_id = sa.Column(saut.UUIDType(binary=False),sa.ForeignKey('user.id',ondelete='CASCADE'))
  deliverys = orm.relationship('Delivery',secondary='delivery_deliveryboy',backref='delivery_boy')

  def __init__(self,user,*args, **kwargs) -> None:
      super().__init__(*args, **kwargs)
      self.user = user

  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
