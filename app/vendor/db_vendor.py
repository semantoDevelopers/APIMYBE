from app.classes.Database import Database
from app.utils.encryption import generate_secret_key_user, shaCryptData


class DatabaseVendor(Database):


    def get_vendors_data_from_email(self,username,password):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM vendors WHERE username=%s AND password=%s"
        tuple = (shaCryptData(username), shaCryptData(password))
        cursor.execute(query,tuple)
        fetched_data = cursor.fetchall()
        if self.check_if_data_is_retrieved(fetched_data):
            data = fetched_data[0]
            conn.close()
            return {
                    'error':None,
                    'message':{
                        'vendor':{
                            'id':data[0],
                            'secret_key':data[1],
                            'shop_name':data[2],
                            'username':data[3],
                            'password':data[4],
                            'data_created':data[6],
                            'media_id':data[7],
                            'stripe_account_id':data[8],
                            'fee':data[9]
                        } 
                    }
            }
        else:
            conn.close()
            return {'error':'Username or password incorrect','message':None}
            
    def get_data_from_id(self,id):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM vendors WHERE id=%s"
        tuple = (id)
        cursor.execute(query,tuple)
        fetched_data = cursor.fetchall()
        if self.check_if_data_is_retrieved(fetched_data):
            data = fetched_data[0]
            conn.close()
            return {
                    'error':None,
                    'message':{
                        'vendor':{
                            'id':data[0],
                            'secret_key':data[1],
                            'shop_name':data[2],
                            'username':data[3],
                            'password':data[4],
                            'data_created':data[6],
                            'media_id':data[7],
                            'stripe_account_id':data[8],
                            'fee':data[9]
                        } 
                    }
            }
        else:
            conn.close()
            return {'error':'Username or password incorrect','message':None}


    def register_vendors_data(self,data):
        conn, cursor = self.getConnection()
        if(self.get_vendors_data_from_email(data['username'],data['password']))['error']==None:
            return {'error':None,'message':'Vendor already registered'}
        else:
           query = "INSERT INTO vendors(shop_name,username,password,media_id,stripe_account_id,fee,secret_key) VALUES(%s,%s,%s,%s,%s,%s,%s)"
           tuple = (data['shop_name'], shaCryptData(data['username']), shaCryptData(data['password']), data['media_id'], data['stripe_account_id'], data['fee'], generate_secret_key_user())
           try:
               cursor.execute(query,tuple)
               conn.commit()
               conn.close()
               return {'error':None, 'message':'Vendor registered successfully' }
           except Exception as e:
               return {'error':str(e), 'message':'There was an error during the vendor registration'}


            

     
