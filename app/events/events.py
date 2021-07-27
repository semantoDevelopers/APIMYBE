from app.classes.PaymentStatus import PaymentStatus
from app.utils.adapter import double_to_stripe_value
from app.stripe_tasks.stripe_functions import get_balance_available, transfer_money
from app.events.db_events import DatabaseEvents



db_events = DatabaseEvents()





def check_transaction():
     pending_transactions = db_events.get_transactions_in_pending()['message']
     balance_available = get_balance_available()
     for transaction in pending_transactions:
        #print(transaction)
        if double_to_stripe_value(transaction['amount']) <= balance_available:
            db_events.change_transaction_status(PaymentStatus.COMPLETED, transaction['id'])
            transfer_money(transaction['account_stripe'], amount=transaction['amount'],fee=transaction['fee'])
            print(f"Account: {transaction['account_stripe']} Amount:{transaction['amount']} Fee: {transaction['fee']}")

        else:
            print('no founds')
            break

