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
        query = "INSERT INTO products(name,price,categories_id,models_id,vendors_id,media_id,is_available,is_stocked,stock_quantity,data_created) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        pass    