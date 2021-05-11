from flask import Blueprint,request
from .db_products import DatabaseProducts
from utils.checkheaders import check_headers,RequestType
from utils.errors import * 
from dotenv import load_dotenv
import os

products = Blueprint('products',__name__)
load_dotenv()
secret_key = os.environ['API_SECRET_KEY']

db_products = DatabaseProducts()



#Route for getting all products
@products.route('/',methods=['GET'])
def get_all_products():
    pass

#Route for get filtered products by storeid
@products.route('/<int:storeid>',methods=['GET'])
def get_products_of_store(storeid):
    pass

#Route for get filtered products by category id
@products.route('/<int:catid>',methods=['GET'])
def get_products_of_category(catid):
    pass

#Route for getting categories
@products.route('/categories',methods=['GET'])
def get_categories():
    pass


##ADMIN ROUTES##

 
#Route for posting products
@products.route('/', methods=['POST'])
def post_products():
    check_result = check_headers(request,secret_key,RequestType.JSON)
    if check_result==200:
        data = db_products.register_product(request.json)
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400   

#Route for posting categories
@products.route('/categories',methods=['POST'])
def post_categories():
    check_result = check_headers(request,secret_key,RequestType.JSON)
    if check_result==200:
        data = db_products.register_categories(request.json)
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400    

#Route for posting categories
@products.route('/macros',methods=['POST'])
def post_macros():
    check_result = check_headers(request,secret_key,RequestType.JSON)
    if check_result==200:
        data = db_products.register_macros(request.json)
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400


