from enum import Enum
from .errors import *
import traceback

class RequestType(Enum):
    JSON = 1
    FORM = 2


def check_headers(request, secret_key, type):
    
    try:
        secret_key_to_check = request.headers['SECRETKEY']
        print(secret_key_to_check == secret_key)
        if secret_key_to_check == secret_key:
            print(request.headers['Content-Type']+'content')
            print(request.method)
            if request.method=="GET":
                return 200
            elif 'application/json' in request.headers['Content-Type'] and type.value==1 :
                return 200
            elif 'multipart/form-data' in request.headers['Content-Type'] and type.value==2 :
                return 200
            
            else:
                return 400
    except Exception as e:
        traceback.print_exc()
        return 403


def giveResponse(data,secret_key,request,request_type=RequestType.JSON):
    print(secret_key)
   # print(data)
    check_result = check_headers(request,secret_key,request_type)
    if check_result==200:
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400
