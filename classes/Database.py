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
