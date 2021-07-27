from flask import Blueprint,request
import os
from app.user.db_user import DatabaseUser
from dotenv import load_dotenv
from app.utils.checkheaders import giveResponse, RequestType
from app.utils.errors import error400,error403

user = Blueprint('user',__name__)
load_dotenv()
secret_key = os.environ['API_SECRET_KEY']
db_user = DatabaseUser()

@user.route('/login',methods=['POST'])
def login():
     return giveResponse(db_user.get_user_data(request.json['email'],request.json['password']),secret_key,request,RequestType.JSON)

@user.route('/register',methods=['POST'])
def register():
    return giveResponse(db_user.register_user_data(request.json),secret_key,request,RequestType.JSON)

@user.route('/',methods=['PUT'])
def modify_user_data():
    return giveResponse(db_user.modify_user_data(request.json,request.headers['USERKEY']),secret_key,request,RequestType.JSON)
