from flask import Blueprint,request
from .db_order import DatabaseOrder

order = Blueprint('order',__name__)

db_order = DatabaseOrder()

@order.route('/<int:userid>',methods=['GET'])
def get_order_from_user(user_id):
    pass

@order.route('/',methods=['POST'])
def create_order():
    pass