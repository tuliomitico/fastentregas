from http import HTTPStatus

from flask import jsonify, request

from modules.employee.services.create_employee_service import CreateEmployeeService
from schemas.employee_schema import EmployeeSchema

class CreateEmployeeController():
  def handle(self):
    data = request.get_json()
    try:
      employee = CreateEmployeeService().execute(data['name'],data['telephone'],data['shop'])
    except Exception as e:
      return jsonify(error=str(e)), HTTPStatus.BAD_REQUEST
    employee_schema = EmployeeSchema()
    return jsonify(data=employee_schema.dump(employee)), HTTPStatus.CREATED
