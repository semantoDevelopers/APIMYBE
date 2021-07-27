from flaskext.mysql import MySQL 



class DatabaseModel:

    def __init__(self):
        self.mysql = MySQL()

    def config(self, app):
        self.mysql.init_app(app)

    def getConnection(self):
        conn = self.mysql.connect()
        cursor = conn.cursor()
        return conn, cursor

    def register_model(self,file_url,size):
        conn, cursor = self.getConnection()
        query = "INSERT INTO media(url,size) VALUES(%s,%s)"
        tuple = (file_url,size)
        try:
            cursor.execute(query,tuple)
            id = conn.insert_id()
            conn.commit()
            conn.close()
            return {'error':None,'message':'Product created','id_created':id}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the media'}        