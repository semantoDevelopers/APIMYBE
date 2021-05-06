from flask import Blueprint,request
import os
from .db_user import DatabaseUser
from utils.checkheaders import check_headers
from utils.errors import error400,error403

user = Blueprint('user',__name__)
secret_key = os.environ['SECRET_KEY']
db_user = DatabaseUser()

@user.route('/login',methods=['POST'])
def login():
    check_result = check_headers(request,secret_key)
    if check_result==200:
        data = db_user.get_user_data(request['email'],request['password'])
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400


@user.route('/register',methods=['POST'])
def register():
    check_result = check_headers(request,secret_key)
    if check_result==200:
        data = db_user.register_user_data(request.json)
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400



@user.route('/<id:int>',methods=['PUT'])
def modify_user_data(id):
    check_result = check_headers(request,secret_key)
    if check_result==200:
        data = db_user.modify_user_data(request.json,request.headers['USERKEY'])
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400