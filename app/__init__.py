import os
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from app.user.app import user,db_user
from app.order.app import order,db_order
from app.products.app import products,db_products
from app.review.app import review,db_review
from app.payment.app import payment
from app.media.app import media,db_media
from app.models.app import models,db_models
from app.stripe_tasks import stripe_functions
from app.vendor.app import vendor,db_vendor
from app.events.events import check_transaction,db_events



app = Flask(__name__)
app.config['MYSQL_DATABASE_USER']=os.environ['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD']=os.environ['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB']=os.environ['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST']=''
app.config['UPLOAD_MEDIA_FOLDER'] = './uploads/medias'
app.config['UPLOAD_MODELS_FOLDER'] = './uploads/models'


#DATABASE BLUEPRINTS COMMUNICATION CONFIGURATION 
db_user.config(app)
db_review.config(app)
db_products.config(app)
db_order.config(app)
db_media.config(app)
db_models.config(app)
db_vendor.config(app)
db_events.config(app)


#REGISTER BLUEPRINTS
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(order, url_prefix='/order')
app.register_blueprint(products,url_prefix='/products')
app.register_blueprint(review,url_prefix='/review')
app.register_blueprint(payment,url_prefix='/payment')
app.register_blueprint(media,url_prefix='/media')
app.register_blueprint(models,url_prefix='/models')
app.register_blueprint(vendor,url_prefix='/vendor')




#SCHEDULER FOR TASK 
scheduler = BackgroundScheduler()
scheduler.add_job(func=check_transaction, trigger="interval", seconds=10)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())
