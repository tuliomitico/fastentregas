from http import HTTPStatus

from flask import request, jsonify

from modules.deliveryboy.services.create_password_delivery_boy_service import CreatePasswordDeliveryBoyService
from schemas.delivery_boy_schema import DeliveryBoySchema

class CreatePasswordDeliveryBoyController():
  def handle(self):
    data = request.get_json()
    delivery_boy_schema = DeliveryBoySchema()
    try:
      delivery_boy = CreatePasswordDeliveryBoyService().execute(telephone=data['telephone'],password=data['password'])
    except Exception as e:
      return {'error': str(e)}, HTTPStatus.BAD_REQUEST
    return jsonify(data=delivery_boy_schema.dump(delivery_boy)), HTTPStatus.CREATED
