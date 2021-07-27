from app.utils.productsLoad import listOfMapProduct
from flaskext.mysql import MySQL 
from app.classes.Database import Database
from app.utils.productsLoad import listOfMapProduct


class DatabaseProducts(Database):





    def get_all_products(self):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM products"
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            conn.close()
            return {'error':None,'products':listOfMapProduct(data)}
        except Exception as e:
            return {'error':str(e),'message':'There was an error retrieving product'}

    def get_filtered_by_categories_products(self,catid):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM products WHERE categories_id=%s"
        tuple=(catid)
        try:
            cursor.execute(query,catid)
            data = cursor.fetchall()
            conn.close()
            return {'error':None,'products':listOfMapProduct(data)}
        except Exception as e:
            return {'error':str(e),'message':'There was an error retrieving product'}

    def get_filtered_by_store_products(self,storeid):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM products WHERE vendors_id=%s"
        tuple = (storeid)
        try:
            cursor.execute(query,tuple)
            data = cursor.fetchall()

            conn.close()
            return {'error':None,'products':listOfMapProduct(data)}
        except Exception as e:
            return {'error':str(e),'message':'There was an error retrieving product'}


    def get_all_categories(self):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM categories"
        try:
            cursor.execute(query)
            data = cursor.fetchall()
            conn.close()
            return {'error':None,'categories':data}
        except Exception as e:
            return {'error':str(e),'message':'There was an error retrieving categories'}




    def register_product(self,data):
        conn,cursor = self.getConnection()
        query = "INSERT INTO products(name,price,categories_id,models_id,vendors_id,media_id,is_available,is_stocked,stock_quantity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        tuple = (data['name'],data['price'],data['categories_id'],data['models_id'],data['vendors_id'],data['media_id'],data['is_available'],data['is_stocked'],data['stock_quantity'])
        try:
            cursor.execute(query,tuple)
            conn.commit()
            conn.close()
            return {'error':None,'message':'Product created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the product'}
    

    def register_variant_product(self,data):
        conn,cursor = self.getConnection()
        query = "INSERT INTO variant_products(id_product,price,categories_id,models_id,vendors_id,media_id,is_available,is_stocked,stock_quantity) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        tuple = (data['id_product'],data['price'],data['categories_id'],data['models_id'],data['vendors_id'],data['media_id'],data['is_available'],data['is_stocked'],data['stock_quantity'])
        try:
            cursor.execute(query,tuple)
            conn.commit()
            conn.close()
            return {'error':None, 'message':f"Variant of {data['id_product']} product created"}
        except Exception as e:
            return {'error':str(e),'message':'There was an error on creating the variant of product'}

    def register_categories(self,data):
        conn, cursor = self.getConnection()
        if 'media_id' in data.keys():
            query = "INSERT INTO categories(name,media_id,macro_id) VALUES(%s,%s,%s)"
            tuple = (data['name'],data['media_id'],data['macro_id'])
        else:
            query = "INSERT INTO categories(name,macro_id) VALUES(%s,%s)"
            tuple = (data['name'],data['macro_id'])
        try:
            cursor.execute(query,tuple)
            conn.commit()
            conn.close()
            return {'error':None,'message':'Category created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the category'}


    def register_macros(self,data):
        conn, cursor = self.getConnection()
        query = "INSERT INTO macros(name) VALUES(%s)"
        tuple = (data['name'])
        try:
            cursor.execute(query,tuple)#,data['media_id']
            conn.commit()
            conn.close()
            return {'error':None,'message':'Macro created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the macro'}
    def register_attributes(self,data):
        conn, cursor = self.getConnection()
        query = "INSERT INTO attributes(name) VALUES(%s)"
        tuple = (data['name'])
        try:
            cursor.execute(query,tuple)#,data['media_id']
            conn.commit()
            conn.close()
            return {'error':None,'message':'Attributes created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the macro'}
