from http import HTTPStatus

from flask import request, jsonify

from modules.employee.services.create_password_employee_service import CreatePasswordEmployeeService
from schemas.employee_schema import EmployeeSchema

class CreatePasswordEmployeeController():
  def handle(self):
    data = request.get_json()
    employee_schema = EmployeeSchema()
    try:
      employee = CreatePasswordEmployeeService().execute(telephone = data['telephone'], password = data['password'])
    except Exception as e:
      return {'error': str(e)}, HTTPStatus.BAD_REQUEST
    result = employee_schema.dump(employee)
    return jsonify(data=result), HTTPStatus.CREATED
