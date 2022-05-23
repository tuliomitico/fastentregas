from models.employee import Employee
from modules.employee.services.create_password_employee_service import CreatePasswordEmployeeService
from tests.factories import EmployeeFactory, UserFactory

def test_create_password_service(db_session):
  user = UserFactory(telephone='0012345678',password=None).create()
  employee_factory = EmployeeFactory(user=user).create()
  employee = CreatePasswordEmployeeService().execute(telephone=employee_factory.user.telephone,password='qwerty')
  assert [employee] == Employee.query.all()

