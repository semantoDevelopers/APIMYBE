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


def transfer_money(amount=0,fee=0):


    if fee<1:
        amounted_feed = amount*fee
        valid_amount = amount-int(str(amounted_feed).replace('.0',''))
    else:
        valid_fee = int(str(fee).replace('.',''))
        valid_amount = amount-valid_fee
        
        
    strp.Transfer.create(
        amount=valid_amount,
        currency="eur",
        destination = "acct_1IvlLkRGn9H4EfEt", 
    )