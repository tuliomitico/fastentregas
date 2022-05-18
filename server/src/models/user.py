import uuid

import sqlalchemy as sa
import sqlalchemy_utils as saut

from database.db import Base, db_session
class User(Base):
    __tablename__ = 'user'
    id = sa.Column(saut.UUIDType(binary=False),default=uuid.uuid4,primary_key = True)
    name = sa.Column(sa.Text)
    password = sa.Column(sa.Text)
    telephone = sa.Column(sa.Text,unique=True,nullable=False)
    created_at = sa.Column(sa.DateTime(timezone=True),server_default=sa.func.now())
    updated_at = sa.Column(sa.DateTime(timezone=True),server_default=sa.func.now(),onupdate=sa.func.now())

    def __init__(self, name: str, telephone: str, *args, **kwargs) -> None:
        super(User,self).__init__(*args,**kwargs)
        self.name = name
        self.telephone = telephone
        # self.password = password

    def create(self):
        db_session.add(self)
        db_session.commit()
        return self

