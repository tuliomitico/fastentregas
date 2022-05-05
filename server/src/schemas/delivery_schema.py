from models.delivery import Delivery
from .schemas import ma

class DeliverySchema(ma.Schema):
  class Meta:
    model = Delivery
    fields = ['hour','code','date','address','name','telephone','shop','status']
