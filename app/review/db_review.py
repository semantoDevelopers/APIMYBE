from app.classes.Database import Database
from flaskext.mysql import MySQL 


class DatabaseReview(Database):

    def register_review(self,data):
        conn,cursor = self.getConnection()
        query = "INSERT INTO review(comment,point,users_id,products_id) VALUES(%s,%s,%s,%s)"
        tuple = (data['comment'],data['point'],data['users_id'],data['products_id'])
        try:
            cursor.execute(query,tuple)
            conn.commit()
            conn.close()
            return {'error':None,'message':'Review created'}
        except Exception as e:
            return  {'error':str(e),'message':'There was an error on creating the review'}


    