from enum import Enum

class RequestType(Enum):
    JSON = 1
    FORM = 2


def check_headers(request, secret_key, type):
    
    try:
        secret_key_to_check = request.headers['SECRETKEY']
     
        if request.headers['Content-Type'] == 'application/json' and type.value==1 :
            return 200
        elif request.headers['Content-Type'] == 'multipart/form-data' and type.value==2 :
            return 200
        else:
            return 400
    except Exception as e:
        
        return 403


