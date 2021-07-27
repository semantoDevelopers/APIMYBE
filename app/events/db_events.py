from app.classes.Database import Database


class DatabaseEvents(Database):

    def get_transactions_in_pending(self):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM transactions WHERE status=0"
        try:
            cursor.execute(query)
            pending_transactions_from_db= cursor.fetchall()
            pending_transaction_map = []
            for transaction in pending_transactions_from_db:
                pending_transaction_map.append(
                    {
                        "id":transaction[0],
                        "account_stripe":transaction[1],
                        "status":transaction[2],
                        "created_at":transaction[3],
                        "vendor_id":transaction[4],
                        "amount":transaction[5],
                        "fee":transaction[6]
                    }
                )
            return {"error":None, "message":pending_transaction_map}
        except Exception as e:
            return {"error":str(e), "message":"There was an error getting the transactions"}

    def change_transaction_status(self,status,id):
        conn, cursor = self.getConnection()
        query = f"UPDATE transactions SET status=1 WHERE id={id}"
      
        try:
            cursor.execute(query)
            conn.commit()
            conn.close()
            return {"error":None, "message":f"Status of the payment changed succesfully in {status}"}
        except Exception as e:
            return {"error":str(e), "message":"Error while changing status of the transaction"}


    def get_all_transactions(self):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM transactions"
        try:
            cursor.execute(query)
            all_transactions_from_db= cursor.fetchall()
            all_transaction_map = []
            for transaction in all_transactions_from_db:
                all_transaction_map.append(
                    {
                        "id":transaction[0],
                        "account_stripe":transaction[1],
                        "status":transaction[2],
                        "created_at":transaction[3],
                        "vendor_id":transaction[4],
                        "amount":transaction[5]
                    }
                )
            return {"error":None, "message":all_transaction_map}
        except Exception as e:
            return {"error":str(e), "message":"There was an error getting the transactions"}
            
    def get_all_transactions_id(self,vendor_id):
        conn, cursor = self.getConnection()
        query = f"SELECT * FROM transactions WHERE vendor_id={vendor_id}"
        try:
            cursor.execute(query)
            all_transactions_from_db= cursor.fetchall()
            all_transaction_map = []
            for transaction in all_transactions_from_db:
                all_transaction_map.append(
                    {
                        "id":transaction[0],
                        "account_stripe":transaction[1],
                        "status":transaction[2],
                        "created_at":transaction[3],
                        "vendor_id":transaction[4],
                        "amount":transaction[5]
                    }
                )
            return {"error":None, "message":all_transaction_map}
        except Exception as e:
            return {"error":str(e), "message":"There was an error getting the transactions"}
        

    def get_transactions_with_error(self):
        pass
    
