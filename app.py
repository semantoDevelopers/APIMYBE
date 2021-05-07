from flask import Flask
import os
from user.app import user,db_user
from order.app import order,db_order
from products.app import products,db_products
from review.app import review,db_review
from payment.app import payment

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER']=os.environ['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD']=os.environ['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB']=os.environ['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST']=''


#DATABASE BLUEPRINTS COMMUNICATION CONFIGURATION 
db_user.config(app)
db_review.config(app)
db_products.config(app)
db_order.config(app)


#REGISTER BLUEPRINTS
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(products,url_prefix='/products')
app.register_blueprint(review,url_prefix='/review')
app.register_blueprint(payment,url_prefix='/payment')


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)