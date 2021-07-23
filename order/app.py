from utils.checkheaders import RequestType, giveResponse
from flask import Blueprint,request
from .db_order import DatabaseOrder
from stripe_tasks.stripe_functions import pay,transfer_money
import os


order = Blueprint('order',__name__)

db_order = DatabaseOrder()
secret_key = os.environ['API_SECRET_KEY']

@order.route('/<int:user_id>',methods=['GET'])
def get_order_from_user(user_id):
    return giveResponse(db_order.get_orders_user_id(user_id,request.headers['USERKEY']),secret_key,request,RequestType.JSON,)

@order.route('/<payment_method>',methods=['POST'])
def create_order(payment_method):
    print(payment_method)
    db_order.register_transactions_of_order(request.json['order'],payment_method)
    return giveResponse(db_order.register_new_order(request.json,request.headers['USERKEY']),secret_key,request,RequestType.JSON,)

@order.route('/transactions/all', methods=['GET'])
def get_all_transaction():
    return giveResponse(db_order.get_transactions(),secret_key,request,RequestType.JSON)
    

@order.route('/test')
def test():
    transfer_money(amount=200,fee=0.2)
    return 'Transfer made'