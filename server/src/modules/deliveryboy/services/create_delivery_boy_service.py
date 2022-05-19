import re

from models.user import User
from models.deliveryboy import DeliveryBoy

class CreateDeliveryBoyService():
  def execute(self, name: str, telephone: str):
    formatted_telephone = re.sub(r'\s+',"",telephone) # Remove white spaces
    user_already_exists: User = User.query.filter_by(telephone = formatted_telephone).first()
    print(user_already_exists)
    if user_already_exists:
      delivery_boy_already_exists = DeliveryBoy.query.filter_by(user_id = user_already_exists.id).first()
      if delivery_boy_already_exists:
        raise Exception('Delivery boy already exists.')
    user = User(name=name,telephone=telephone)
    delivery_boy = DeliveryBoy(user=user).create()
    return delivery_boy
