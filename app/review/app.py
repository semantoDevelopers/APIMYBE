from flask import Blueprint,request
from app.review.db_review import DatabaseReview
from app.utils.checkheaders import giveResponse
from dotenv import load_dotenv
import os

review = Blueprint('review',__name__)
load_dotenv()
secret_key = os.environ['API_SECRET_KEY']
db_review = DatabaseReview()



@review.route('/<int:prodid>',methods=['GET'])
def get_reviews_of_prod(prodid):
    return giveResponse(db_review.register_review(request.json),secret_key,request)

@review.route('/<int:prodid>',methods=['POST'])
def post_review_of_prod(prodid):
    pass
  #  return giveResponse()

@review.route('/<int:prodid>/<int:userid>',methods=['PUT'])
def modify_review_of_prod(prodid,userid):
    pass