from flaskext.mysql import MySQL
from pymysql import cursors 
from app.classes.Database import Database
from app.stripe_tasks.stripe_functions import pay
import json
from ast import literal_eval
import traceback

class DatabaseOrder(Database):

    def get_transactions(self):
        conn, cursor = self.getConnection()
        query = "SELECT * FROM transactions"
        try:
            cursor.execute(query)
            transaction = cursor.fetchall()
            json_transactions = []
            for trans in transaction:
                json_transactions.append({"id":trans[0],"stripe_account_id":trans[1],"status":trans[2], "date_created":trans[3], "vendor_id":trans[4], "amount":trans[5],"fee":trans[6]})
            return {'error': None, 'message':json_transactions}
        except Exception as e:
            return {'error': str(e), 'message':"There was an error during getting the transactions"}


    def register_transactions_of_order(self,orders,payment_method):
        conn, cursor = self.getConnection()
        transactions = {}
        total_amount = 0
        for order in orders:
            query_get_product_details = f"SELECT price, vendors_id FROM products WHERE id={order['product_id']}"
            cursor.execute(query_get_product_details)
            product = cursor.fetchall()[0]
            total_amount+=product[0]    
            if product[1] in transactions:
                transactions[product[1]]+=product[0]
            else:
                transactions[product[1]]=0
            
        for key in transactions.keys():
            query_get_stripe_account_id = f"SELECT stripe_account_id, fee FROM vendors WHERE id={key}"
            cursor.execute(query_get_stripe_account_id)
            stripe_account = cursor.fetchall()[0]
            query_create_transaction = f"INSERT INTO transactions(account_stripe,status,vendor_id,amount) VALUES('{str(stripe_account[0])}',0,{str(key)},{transactions[key]},{stripe_account[1]})"
            cursor.execute(query_create_transaction)
            conn.commit()
        pay(payment_method,int(str(total_amount).replace('.','')),)
        print(transactions)
        conn.close()
        

    def register_new_order(self,data,secret_key):
        conn, cursor = self.getConnection()
        query_check_secret_key="SELECT * FROM users WHERE id=%s AND secret_key=%s"
        
        tuple_check_secret_key = (data['user_id'],secret_key)
        print(type(data['order']))
        orderString = ""
        for order in data['order']:
            orderString+=str(order)
        print(orderString)
        tuple_register_order = (orderString,data['user_id'])
        try:
            cursor.execute(query_check_secret_key, tuple_check_secret_key)
            fetchedData = cursor.fetchall()
            if len(fetchedData)>0:
                orderS = str(data['order']).replace("'","*")
                query_register_order=f"INSERT INTO orders(order_content,user_id) VALUES('{orderS}',{data['user_id']})"
                print(query_register_order)
                cursor.execute(query_register_order)
                conn.commit()
                conn.close()
                return {'error':None, 'message':'Ordered successfully registered'}
            else:
                raise()
        except Exception as e:
                traceback.print_exc()
                return {'error':str(e), 'message':'There was an error during registration'}


    def get_orders_user_id(self,user_id,secret_key):
        conn, cursor = self.getConnection()
        query_check_secret_key="SELECT * FROM users WHERE id=%s AND secret_key=%s"
        query_get_order="SELECT * FROM orders WHERE user_id = %s"
        tuple_check_secret_key = (user_id,secret_key)
        tuple_get_order = (user_id)
        try:
            cursor.execute(query_check_secret_key, tuple_check_secret_key)
            fetchedData = cursor.fetchall()
            if len(fetchedData[0])>0:
                cursor.execute(query_get_order,tuple_get_order)
                orders = []
                orders_from_db = cursor.fetchall()
                for order in orders_from_db:
                    order_translated = json.dumps(literal_eval(order[1].replace('*','"')))
                    print(order_translated)
                    orders.append({
                        "id":order[0],
                        "order":literal_eval(order_translated),
                        "state":order[2],
                        "user_id":order[3],
                        "data_created":order[4]
                    })


                conn.commit()
                conn.close()
                return {'error':None, 'message':orders}
        except Exception as e:
                traceback.print_exc()
                return {'error':str(e), 'message':'There was an error during registration'}
