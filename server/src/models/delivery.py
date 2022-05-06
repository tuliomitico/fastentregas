
import enum

import sqlalchemy as sa
import sqlalchemy_utils as saut

from database.db import Base, db_session

class StatusType(enum.Enum):
  avaliable = 0
  catched = 1
  closed = 2
class Delivery(Base):
  __tablename__ = 'delivery'

  id = sa.Column(sa.BigInteger,primary_key=True)
  hour = sa.Column(sa.DateTime(timezone=True),server_default=sa.func.now())
  # address
  telephone=sa.Column(sa.Text)
  name=sa.Column(sa.Text)
  shop=sa.Column(sa.Text)
  status = sa.Column(saut.ChoiceType(StatusType,impl=sa.Integer()))

  def __init__(self, id: int, telephone: str, name: str, shop: str, status: int,**kwargs):
    self.id = id

    self.telephone = telephone
    self.name = name

    self.shop = shop

    self.status = status

  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
   # 0 seria não pego
   # 1 já foi pego
   # 2 finalizado por motivo qlqr
