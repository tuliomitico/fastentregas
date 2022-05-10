from flask import Blueprint, request

from middlewares.auth import auth
from models.delivery import Delivery
from modules.users.controllers.authenticate_user_controller import AuthenticateUserController
from modules.users.controllers.create_user_controller import CreateUserController
from modules.users.controllers.get_user_controller import GetUserController
from schemas.delivery_schema import DeliverySchema

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
  delivery_schema = DeliverySchema()
  deliverys_schema = DeliverySchema(many=True)
  if request.method == 'POST':
    data = request.get_json()
    delivery_data = delivery_schema.load(data)
    delivery = Delivery(**delivery_data).create()
    return {'delivery':delivery_schema.dump(delivery)}, 202
  else:
    delivery = Delivery.query.all()
    return {'deliverys': deliverys_schema.dump(delivery)}

@blp.route('/')
def index():
  return {"Hello":"World"}, 200

# ! Test route
@blp.route('/user',methods=['GET'])
@auth.login_required
def get_users():
  users = GetUserController().handle()
  return {**users[0],'user': auth.current_user()}, users[1]
