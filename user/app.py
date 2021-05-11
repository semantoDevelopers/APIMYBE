from flask import Blueprint,request
import os
from .db_user import DatabaseUser
from dotenv import load_dotenv
from utils.checkheaders import check_headers,RequestType
from utils.errors import error400,error403

user = Blueprint('user',__name__)
load_dotenv()
secret_key = os.environ['API_SECRET_KEY']
db_user = DatabaseUser()

@user.route('/login',methods=['POST'])
def login():
    check_result = check_headers(request,secret_key,RequestType.JSON)
    if check_result==200:
        data = db_user.get_user_data(request.json['email'],request.json['password'])
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400


@user.route('/register',methods=['POST'])
def register():
    check_result = check_headers(request,secret_key,RequestType.JSON)
    if check_result==200:
        data = db_user.register_user_data(request.json)
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400



@user.route('/',methods=['PUT'])
def modify_user_data():
    check_result = check_headers(request,secret_key,RequestType.JSON)
    if check_result==200:
        data = db_user.modify_user_data(request.json,request.headers['USERKEY'])
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400
