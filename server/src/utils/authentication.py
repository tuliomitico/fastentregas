from functools import wraps
from http import HTTPStatus

from flask import g
from flask_jwt_extended import verify_jwt_in_request, current_user

from models.admin import Admin
from models.deliveryboy import DeliveryBoy
from models.employee import Employee

class Auth():
  def admin_required(self,f=None):
    def admin_required_internal(f):
      @wraps(f)
      def decorator(*args,**kwargs):
        verify_jwt_in_request()
        admin_exists = Admin.query.filter_by(user_id=current_user.id).first()
        if admin_exists:
          return f(*args,**kwargs)
        else:
          return {'message': 'Admins only.'}, HTTPStatus.FORBIDDEN
      return decorator
    if f:
      return admin_required_internal(f)
    return admin_required_internal

  def employee_required(self,f=None):
    def employee_required_internal(f):
      @wraps(f)
      def decorator(*args,**kwargs):
        verify_jwt_in_request()
        employee_exists = Employee.query.filter_by(user_id=g.user['id']).first()
        if employee_exists:
          return f(*args,**kwargs)
        else:
          return {'message': 'Employee only.'}, HTTPStatus.FORBIDDEN
      return decorator
    if f:
      return employee_required_internal(f)
    return employee_required_internal

  def admin_or_employee_required(self,f=None):
    def admin_or_employee_required_internal(f):
      @wraps(f)
      def decorator(*args,**kwargs):
        verify_jwt_in_request()
        admin_exists = Admin.query.filter_by(user_id=current_user.id).first()
        employee_exists = Employee.query.filter_by(user_id=current_user.id).first()
        if admin_exists or employee_exists:
          return f(*args,**kwargs)
        else:
          return {'message': 'Admin or employee only.'}, HTTPStatus.FORBIDDEN
      return decorator
    if f:
      return admin_or_employee_required_internal(f)
    return admin_or_employee_required_internal

  def deliveryboy_required(self,f=None):
    def deliveryboy_required_internal(f):
      @wraps(f)
      def decorator(*args,**kwargs):
        verify_jwt_in_request()
        deliveryboy_exists = DeliveryBoy.query.filter_by(user_id=current_user.id).first()
        if deliveryboy_exists:
          return f(*args,**kwargs)
        else:
          return {'message': 'Delivery boy only.'}, HTTPStatus.FORBIDDEN
      return decorator
    if f:
      return deliveryboy_required_internal(f)
    return deliveryboy_required_internal

  def current_user(self):
    if hasattr(g,'user'):
      return g.user['name']
