from flask import request, jsonify
from http import HTTPStatus

from modules.deliverys.services.create_delivery_service import CreateDeliveryService
from schemas.delivery_schema import DeliverySchema

class CreateDeliveryController():
  def handle(self):
    data = request.get_json()
    delivery = CreateDeliveryService().execute(
      data['name'],
      data['shop'],
      data['telephone'],
      data['status'],
      data['district'],
      data['st_or_av'],
      data['number']
    )
    delivery_schema = DeliverySchema()
    return jsonify({'delivery': delivery_schema.dump(delivery)}), HTTPStatus.CREATED
