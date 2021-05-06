from flaskext.mysql import MySQL 



class DatabaseOrder:

    def __init__(self):
        self.mysql = MySQL()

    def config(self, app):
        self.mysql.init_app(app)