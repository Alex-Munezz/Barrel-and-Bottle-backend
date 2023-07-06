from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

from flask_migrate import Migrate
from models import db, Review,Drink
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
# db = SQLAlchemy(app)

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()
    drinks_list = []
    for drink in drinks:
        drinks_data = {
            'id': drink.id,
            'cover':drink.cover,
            'name': drink.name,
            'percentage': drink.percentage,
            'breweries': drink.breweries,
            'price':drink.price
            
        }
        drinks_list.append(drinks_data)
    return jsonify(drinks_list)

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    reviews_list = []
    for review in reviews:
        reviews_data = {
            'id': review.id,
            'drink_id': review.drink_id,
            'customer_id': review.customer_id,
            'review': review.review
            
        }
        reviews_list.append(reviews_data)
    return jsonify(reviews_list)

@app.route('/drinks/<int:drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    drink = Drink.query.get(drink_id)
    if drink:
        db.session.delete(drink)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Drink not found'}), 404

if __name__ == '__main__':
    app.run(port=5555)



# # from routes import reviews_blueprint
# app.register_blueprint(reviews_blueprint)
