from flask import Blueprint,request
from .db_products import DatabaseProducts

products = Blueprint('products',__name__)

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
    pass

#Route for posting categories
@products.route('/categories',methods=['POST'])
def post_categories():
    pass

