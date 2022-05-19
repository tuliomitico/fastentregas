from passlib.hash import bcrypt

from database.db import db_session
from models.deliveryboy import DeliveryBoy
from models.user import User

class CreatePasswordDeliveryBoyService():
  def execute(self, telephone: str, password: str):
    user = User.query.filter_by(telephone=telephone).first()
    if user:
      if user.password:
        raise Exception('Password already created.')
      user.password = bcrypt.using(rounds=10).hash(password)
      db_session.commit()
      delivery_boy = DeliveryBoy.query.filter_by(user_id=user.id).first()
      return delivery_boy
    raise Exception('No user found with this phone number')
