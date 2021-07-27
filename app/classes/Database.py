from flaskext.mysql import MySQL 
class Database:

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
