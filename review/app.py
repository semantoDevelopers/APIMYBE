from flask import Blueprint,request
from .db_review import DatabaseReview
from dotenv import load_dotenv
import os

review = Blueprint('review',__name__)
load_dotenv()
secret_key = os.environ['API_SECRET_KEY']
db_review = DatabaseReview()



@review.route('/<int:prodid>',methods=['GET'])
def get_reviews_of_prod(prodid):
    pass

@review.route('/<int:prodid>',methods=['POST'])
def post_review_of_prod(prodid):
    pass

@review.route('/<int:prodid>/<int:userid>',methods=['PUT'])
def modify_review_of_prod(prodid,userid):
    pass