from flask import Blueprint, request

from middlewares.auth import auth
from modules.deliveryboy.controllers.create_delivery_boy_controller import CreateDeliveryBoyController
from modules.deliveryboy.controllers.create_password_delivery_boy_controller import CreatePasswordDeliveryBoyController
from modules.deliveryboy.controllers.get_delivery_boy_controller import GetDeliveryBoyController
from modules.deliveryboy.controllers.get_delivery_boys_controller import GetDeliveryBoysController
from modules.deliverys.controllers.create_delivery_controller import CreateDeliveryController
from modules.deliverys.controllers.get_delivery_controller import GetDeliveryController
from modules.employee.controllers.create_employee_controller import CreateEmployeeController
from modules.employee.controllers.create_password_employee_controller import CreatePasswordEmployeeController
from modules.users.controllers.authenticate_user_controller import AuthenticateUserController
from modules.users.controllers.create_user_controller import CreateUserController
from modules.users.controllers.get_user_controller import GetUserController

blp = Blueprint('index',__name__)
blp_auth = Blueprint('auth',__name__)
blp_delivery = Blueprint('delivery',__name__)

# ======================
# Authentication routes
# ======================
@blp_auth.route('/login',methods=['POST'])
def login():
  user = AuthenticateUserController().handle()
  return user

@blp_auth.route('/register',methods=['POST'])
def register():
  "Create a new user"
  user = CreateUserController().handle()
  return user

# ======================
# Delivery routes
# ======================
@blp_delivery.route('/deliver',methods=['GET','POST'])
def delivery():
  if request.method == 'POST':
    delivery = CreateDeliveryController().handle()
    return delivery
  else:
    delivery = GetDeliveryController().handle()
    return delivery

# ======================
# Delivery Boy routes
# ======================
@blp.route('/delivery_boy/<int:id>')
def delivery_boy_get(id):
  delivery_boy = GetDeliveryBoysController().handle(id)
  return delivery_boy

@blp.route('/delivery_boy')
def delivery_boy():
  delivery_boy = GetDeliveryBoyController().handle()
  return delivery_boy

@blp.route('/register/delivery_boy',methods=['POST'])
def create_motoboy():
  delivery_boy = CreateDeliveryBoyController().handle()
  return delivery_boy

@blp.route('/delivery_boy/create_password',methods=['POST'])
def create_password():
  delivery_boy = CreatePasswordDeliveryBoyController().handle()
  return delivery_boy

# ====================
# Employee routes
# ====================
@blp.route('/employee',methods=['GET','POST'])
def employee():
  employee = CreateEmployeeController().handle()
  return employee

@blp.route('/employee/create_password',methods=['POST'])
def employee_create_password():
  employee = CreatePasswordEmployeeController().handle()
  return employee

@blp.route('/')
def index():
  return {"Hello":"World"}, 200

# ! Test route
@blp.route('/users',methods=['GET'])
@auth.login_required
def get_users():
  users = GetUserController().handle()
  return {**users[0],'user': auth.current_user()}, users[1]

@blp.route('/user')
@auth.login_required
def get_current_user():
  return {'user': {'name': auth.current_user() }}
