from models.deliveryboy import DeliveryBoy
from models.user import User

class ViewDeliveryGotService():
  def execute(self, name: str):
    user = User.query.filter_by(name = name).first()
    delivery_boy = DeliveryBoy.query.filter_by(user_id=user.id).first()
    return delivery_boy
