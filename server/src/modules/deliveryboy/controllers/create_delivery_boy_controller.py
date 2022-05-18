from http import HTTPStatus

from flask import jsonify, request

from modules.deliveryboy.services.create_delivery_boy_service import CreateDeliveryBoyService
from schemas.delivery_boy_schema import DeliveryBoySchema

class CreateDeliveryBoyController():
  def handle(self):
    data = request.get_json()
    try:
      delivery_boy = CreateDeliveryBoyService().execute(data['name'],data['telephone'])
    except Exception as e:
      return jsonify(error=str(e)), HTTPStatus.BAD_REQUEST
    delivery_boy_schema = DeliveryBoySchema()
    return jsonify(data=delivery_boy_schema.dump(delivery_boy)), HTTPStatus.CREATED
