from flask import Blueprint, request
from app.utils.encryption import shaCryptData
from app.utils.checkheaders import RequestType, giveResponse
from app.vendor.db_vendor import DatabaseVendor
import os

vendor = Blueprint('vendor',__name__)
db_vendor = DatabaseVendor()

secret_key = os.environ['API_SECRET_KEY']


@vendor.route('/', methods=['POST'])
def create_vendor():
    return giveResponse(db_vendor.register_vendors_data(request.json),secret_key,request,RequestType.JSON)

@vendor.route('/', methods=['GET'])
def get_from_email_and_password():
    return giveResponse(db_vendor.get_vendors_data_from_email(request.json['username'],request.json['password']),secret_key,request,RequestType.JSON)

@vendor.route('/<vendor_id>', methods=['PUT'])
def modify_vendor_data(vendor_id):
    pass

@vendor.route('/<vendor_id>', methods=['GET'])
def get_vendor_from_id(vendor_id):
    pass

@vendor.route('/all', methods=['GET'])
def get_all_vendors():
    pass


