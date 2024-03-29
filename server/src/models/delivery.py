
import enum

import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as saut

from database.db import Base, db_session
from .address import Address

class StatusType(enum.Enum):
  avaliable = 0
  catched = 1
  closed = 2

class DeliveryType(enum.Enum):
  a = 1
  b = 2
class Delivery(Base):
  __tablename__ = 'delivery'
  id = sa.Column(sa.Integer,primary_key=True)
  hour = sa.Column(sa.DateTime(timezone=True),server_default=sa.func.now())
  address = orm.relationship('Address')
  address_id = sa.Column(sa.ForeignKey('address.id',ondelete='CASCADE'))
  telephone=sa.Column(sa.Text)
  name=sa.Column(sa.Text)
  shop=sa.Column(sa.Text)
  status = sa.Column(saut.ChoiceType(StatusType,impl=sa.Integer()))

  def __init__(
    self,
    telephone: str,
    name: str,
    shop: str,
    status: int,
    *args,
    **kwargs):
    super(Delivery,self).__init__(*args,**kwargs)
    self.telephone = telephone
    self.name = name
    self.shop = shop
    self.status = status

  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
