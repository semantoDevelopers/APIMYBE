from Crypto.Hash import SHA256
import string
import secrets
#From String data return a SHA256 String 
def shaCryptData(data):
    sha = SHA256.new()
    sha.update(data.encode())
    return sha.hexdigest()

def generate_secret_key_user():
    return ''.join(secrets.choice(string.ascii_uppercase+string.ascii_lowercase + string.digits)for i in range(50))