import sqlalchemy as sa
import sqlalchemy.orm as orm
import sqlalchemy_utils as saut

from database.db import Base, db_session
from models.user import User

class Admin(Base):
  __tablename__ = 'admin'
  id = sa.Column(sa.Integer,primary_key=True)
  user = orm.relationship('User')
  user_id = sa.Column(saut.UUIDType(binary = False),sa.ForeignKey('user.id',ondelete='CASCADE'))

  def __init__(self, user ,*args, **kwargs) -> None:
      super().__init__(*args, **kwargs)
      self.user = user

  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
