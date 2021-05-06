from flaskext.mysql import MySQL
import os
from utils.encryption import generate_secret_key_user,shaCryptData
import json

class DatabaseUser:

    def __init__(self):
        self.mysql = MySQL()

    def config(self, app):
        self.mysql.init_app(app)

    def getConnection(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        return conn, cursor

    def check_if_data_is_retrieved(self, data):
        if len(data) < 1:
            return False
        else:
            return True

    def get_user_data(self, email, password):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        tuple = (shaCryptData(email), shaCryptData(password))
        cursor.execute(query, tuple)
        data = cursor.fetchall()[0]
        conn.close()
        if(self.check_if_data_is_retrieved(data)):
            return {'error': None, 'user': {'id': data[0], 'secret_key': data[1], 'name': data[2], 'surname': data[3], 'email': data[4], 'phone_number': data[6], 'address': data[7], 'fiscal_code': data[8], 'favorites': data[9], 'media_id': data[10]}}
        else:
            return {'error':'Email or Password incorrect','user':{}}


    def register_user_data(self,data):
        conn, cursor = self.getConnection()
        query = "INSERT INTO users(secret_key,name,surname,email,password,phone_number,address,token,favorites) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        tuple = (generate_secret_key_user(),data['name'],data['surname'],shaCryptData(data['email']),shaCryptData(data['password']),shaCryptData(data['phone_number']),shaCryptData(data['address']),json.dumps({}),token)
        try:
            cursor.execute(query,tuple)
            conn.close()
            return {'error':None, 'message':'User registered now confirm with code'}
        except Exception as e:
            return {'error':str(e), 'message':'There was an error during registration'}
        
        
    def modify_user_data(self,data,secret_key):
        conn, cursor = self.getConnection()
        query = "UPDATE users WHERE name=%s,surname=%s,email=%s,password=%s,phone_number=%s,address=%s WHERE secret_key=%s"
        tuple = (data['name'],data['surname'],shaCryptData(data['email']),shaCryptData(data['password']),shaCryptData(data['phone_number']),shaCryptData(data['address']),secret_key)
        try:
            cursor.execute(query,tuple)
            conn.close()
            return {'error':None, 'message':'User data modified succesfully'}
        except Exception as e:
            return {'error':str(e), 'message':'There was an error on modifying data'}
        
        