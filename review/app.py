from flask import Blueprint,request
from .db_review import DatabaseReview

review = Blueprint('review',__name__)

db_review = DatabaseReview()

@review.route('/<prodid:int>',methods=['GET'])
def get_reviews_of_prod(prodid):
    pass

@review.route('/<prodid:int>',methods=['POST'])
def post_review_of_prod(prodid):
    pass

@review.route('/<prodid:int>/<userid:int>',methods=['PUT'])
def modify_review_of_prod(prodid,userid):
    pass