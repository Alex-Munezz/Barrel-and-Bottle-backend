from flask import Blueprint, jsonify

reviews_blueprint = Blueprint('reviews', __name__)

@reviews_blueprint.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    reviews_data = [
        {
            'id': review.id,
            'drink_id': review.drink_id,
            'customer_id': review.customer_id,
            'review': review.review
        }
        for review in reviews
    ]
    return jsonify(reviews_data)
