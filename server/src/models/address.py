import sqlalchemy as sa

from database.db import Base, db_session

class Address(Base):

  __tablename__ = 'address'
  id = sa.Column(sa.Integer,primary_key=True)
  district = sa.Column(sa.String(length=64))
  st_or_av = sa.Column(sa.String(length=256))
  number = sa.Column(sa.Integer)

  def __init__(self,district: str, st_or_av: str, number: int, *args, **kwargs) -> None:
    super(Address,self).__init__(*args,**kwargs)
    self.district = district
    self.st_or_av = st_or_av
    self.number = number


  def create(self):
    db_session.add(self)
    db_session.commit()
    return self
