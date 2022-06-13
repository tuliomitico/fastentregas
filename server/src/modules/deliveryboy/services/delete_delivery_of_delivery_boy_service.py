from database.db import db_session
from models.delivery import Delivery
from models.deliveryboy import DeliveryBoy
from models.user import User

class DeleteDeliveryOfDeliveryBoyService():
  def execute(self, pk: int, name: str) -> None:
    user = User.query.filter_by(name=name).first()
    delivery_boy = DeliveryBoy.query.filter_by(user_id=user.id).first()
    delivery = Delivery.query.get(pk)
    delivery_boy.deliverys.remove(delivery)
    db_session.commit()
    return
