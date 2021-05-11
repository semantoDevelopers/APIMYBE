from flaskext.mysql import MySQL 



class DatabaseProducts:

    def __init__(self):
        self.mysql = MySQL()

    def config(self, app):
        self.mysql.init_app(app)

    def getConnection(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        return conn, cursor

    def register_product(self,data):
        conn,cursor = self.getConnection()
        query = "INSERT INTO products(name,price,categories_id,models_id,vendors_id,media_id,is_available,is_stocked,stock_quantity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        tuple = (data['name'],data['price'],data['categories_id'],data['models_id'],data['vendors_id'],data['media_id'],data['is_available'],data['is_stocked'],data['stock_quantity'])
        try:
            cursor.execute(query,tuple)
            conn.close()
            return {'error':None,'message':'Product created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the product'}

    def register_categories(self,data):
        conn, cursor = self.getConnection()
        query = "INSERT INTO categories(name,media_id,macro_id) VALUES(%s,%s,%s)"
        if 'media_id' in data.keys():
            media = data['media_id']
        else:
            media = None
        tuple = (data['name'],media,data['macro_id'])
        try:
            cursor.execute(query,tuple)
            conn.close()
            return {'error':None,'message':'Category created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the category'}


    def register_macros(self,data):
        conn, cursor = self.getConnection()
        query = "INSERT INTO macros(name) VALUES(%s)"
        tuple = data['name']
        try:
            cursor.execute(query,tuple)#,data['media_id']
            conn.commit()
            conn.close()
            return {'error':None,'message':'Macro created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the macro'}