from models.employee import Employee
from models.user import User
from tests.factories import EmployeeFactory

def test_create_delivery_boy(db_session):
  u = User('Teste','00123456789',password='Teste').create()
  e = Employee(user=u,shop='Loja 0')
  assert [e.create()] == Employee.query.all()

def test_factory():
  employee = EmployeeFactory.build_batch(10)
  assert len(employee) == 10

def test_factory_does_not_affect_database(db_session):
  EmployeeFactory.create()
  assert Employee.query.count() == 0
