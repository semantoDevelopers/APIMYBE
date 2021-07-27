from flaskext.mysql import MySQL
import os
from app.classes.Database import Database
from app.utils.encryption import generate_secret_key_user,shaCryptData
import json

class DatabaseUser(Database):

    def get_user_data(self, email, password):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        tuple = (shaCryptData(email), shaCryptData(password))
        cursor.execute(query, tuple)
        fetchedData = cursor.fetchall()
        if(self.check_if_data_is_retrieved(fetchedData)):

            data = fetchedData[0]
            conn.close()
            return {
                    'error': None,
                    'message':{
                        'user':{
                            'id': data[0],
                            'secret_key':data[1],
                            'name': data[2],
                            'surname': data[3],
                            'email': data[4],
                            'phone_number': data[6],
                            'address': data[7],
                            'fiscal_code': data[8],
                            'favorites': data[9],
                            'media_id': data[10]
                            }
                        }
                    }
        else:
            conn.close()
            return {'error':'Email or Password incorrect','message':None}


    def register_user_data(self,data):
        conn, cursor = self.getConnection()

        if(self.get_user_data(data['email'],data['password'])['error']==None):
            return {'error':None, 'message':'User already registered'}
        else:
            query = "INSERT INTO users(secret_key,name,surname,email,password,phone_number,address,token) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            tuple = (generate_secret_key_user(),data['name'],data['surname'],shaCryptData(data['email']),shaCryptData(data['password']),data['phone_number'],data['address'],data['token'])
            try:
                cursor.execute(query,tuple)
                conn.commit()
                conn.close()
                return {'error':None, 'message':'User registered now confirm with code'}
            except Exception as e:
                return {'error':str(e), 'message':'There was an error during registration'}
        
        
    def modify_user_data(self,data,secret_key):
        conn, cursor = self.getConnection()
        query = "UPDATE users SET name=%s,surname=%s,email=%s,password=%s,phone_number=%s,address=%s WHERE secret_key=%s AND id=%s"
        tuple = (data['name'],data['surname'],shaCryptData(data['email']),shaCryptData(data['password']),data['phone_number'],data['address'],secret_key,id)
        try:
            cursor.execute(query,tuple)
            conn.commit()
            conn.close()
            return {'error':None, 'message':'User data modified succesfully'}
        except Exception as e:
            return {'error':str(e), 'message':'There was an error on modifying data'}
        
        
