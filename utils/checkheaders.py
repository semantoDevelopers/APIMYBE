from enum import Enum
from .errors import *


class RequestType(Enum):
    JSON = 1
    FORM = 2


def check_headers(request, secret_key, type):
    
    try:
        secret_key_to_check = request.headers['SECRETKEY']
        print(secret_key_to_check == secret_key)
        if secret_key_to_check == secret_key:
            print('dio  infame')
            if request.method=="GET":
                return 200
            elif request.headers['Content-Type'] == 'application/json' and type.value==1 :
                return 200
            elif request.headers['Content-Type'] == 'multipart/form-data' and type.value==2 :
                return 200
            
            else:
                return 400
    except Exception as e:
        print(e)
        return 403


def giveResponse(data,secret_key,request,request_type=RequestType.JSON):
    print(secret_key)
    check_result = check_headers(request,secret_key,request_type)
    if check_result==200:
        return data
    else:
        if check_result==403:
            return error403
        elif check_result==400:
            return error400