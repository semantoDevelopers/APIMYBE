from flask import Blueprint,request
from .db_products import DatabaseProducts

products = Blueprint('products',__name__)

db_products = DatabaseProducts()

@products.route('/',methods=['GET'])
def get_all_products():
    pass

@products.route('/<int:storeid>',methods=['GET'])
def get_products_of_store(storeid):
    pass

@products.route('/<int:catid>',methods=['GET'])
def get_products_of_category(catid):
    pass

@products.route('/categories',methods=['GET'])
def get_categories():
    pass