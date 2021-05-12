from flask import Blueprint,request
from .db_products import DatabaseProducts
from utils.checkheaders import giveResponse
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
    return giveResponse(db_products.get_all_products(),secret_key,request)

#Route for get filtered products by storeid
@products.route('/?storeid=<int:storeid>',methods=['GET'])
def get_products_of_store(storeid):
    return giveResponse(db_products.get_filtered_by_store_products(storeid),secret_key,request)


#Route for get filtered products by category id
@products.route('/filter?catid=<int:catid>',methods=['GET'])
def get_products_of_category(catid):
    return giveResponse(db_products.get_filtered_by_categories_products(catid),secret_key,request)

#Route for getting categories
@products.route('/categories',methods=['GET'])
def get_categories():
    return giveResponse(db_products.get_all_categories(),secret_key,request)


##ADMIN ROUTES##

 
#Route for posting products
@products.route('/', methods=['POST'])
def post_products():
    return giveResponse(db_products.register_product(request.json),secret_key,request)
    

#Route for posting categories
@products.route('/categories',methods=['POST'])
def post_categories():
    return giveResponse(db_products.register_categories(request.json),secret_key,request)
    

#Route for posting categories
@products.route('/macros',methods=['POST'])
def post_macros():
    return giveResponse(db_products.register_macros(request.json),secret_key,request)


