

def check_headers(request, secret_key):
    secret_key_to_check = request.headers['SECRETKEY']
    if(secret_key_to_check == secret_key):
        if(request.headers['Content-Type'] == 'application/json'):
            return 200
        else:
            return 400
    else:
        return 403

