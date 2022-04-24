from flask import Blueprint

blp = Blueprint('index',__name__)

@blp.route('/')
def index():
  return {"Hello":"World"}, 200
