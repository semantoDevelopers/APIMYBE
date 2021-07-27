from app.utils.adapter import double_to_stripe_value
from stripe.api_resources import application_fee
from dotenv import load_dotenv
import os
from datetime import datetime
import stripe as strp

api_key = os.environ['STRIPE_API_KEY']

strp.api_key = api_key


def pay(payment_method_id,amount):
    if(payment_method_id):
        print(f'{datetime.now()} Payment method received')
        print(f'{datetime.now()} Running the payment intent')
        payment_intent = strp.PaymentIntent.create(
                amount=amount,
                currency="eur",
                payment_method=payment_method_id,
                payment_method_types= ['card'],
                
                confirm=True,
                )
        print(f'{datetime.now()} Payment Intent created')


def transfer_money(account_stripe,amount=0,fee=0):


    if fee<1:
        amounted_feed = ("%.2f" % (amount-amount*fee))
        
        valid_amount = double_to_stripe_value(amounted_feed)

    else:
        
        valid_amount = double_to_stripe_value("%.2f" % amount)-double_to_stripe_value("%.2f" % fee)
        print(f"Amount: {amount} ValidFee:{fee} ValidAmount = {valid_amount}")
        

    strp.Transfer.create(
      
        amount=valid_amount,
        currency="eur",
        destination = account_stripe, 
    )


def get_balance_available():
    all_balance = strp.Balance.retrieve()
    all_available_balance = all_balance['available']
    return all_available_balance[0]['amount']