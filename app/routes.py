from flask import Blueprint, jsonify

reviews_blueprint = Blueprint('reviews', __name__)
drinks_blueprint = Blueprint('drinks', __name__)

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

@drinks_blueprint.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()
    drinks_data = [
        {
            'id': drink.id,
            'cover':drink.cover,
            'name': drink.name,
            'percentage': drink.percentage,
            'breweries': drink.breweries,
            'price':drink.price
        }
        for drink in drinks
    ]
    return jsonify(drinks_data)
