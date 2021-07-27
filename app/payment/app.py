from flask import Blueprint, request

payment = Blueprint('payment',__name__)


@payment.route('/', methods=['POST'])
def pay():
    pass