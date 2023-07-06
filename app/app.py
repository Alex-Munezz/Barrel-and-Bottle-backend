from flask import Flask, request, make_response, jsonify

from flask_migrate import Migrate
from models import db, Review,Drink, Customer
app = Flask(__name__)
# CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
# db = SQLAlchemy(app)

migrate = Migrate(app, db)
db.init_app(app)

# GET drinks
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

@app.route("/drinks/<int:drink_id>", methods=["GET"])
def get_drink(drink_id):
    drink = Drink.query.filter_by(id=drink_id).first()

    if not drink:
        return jsonify({}), 404

    drink_data = {
            'id': drink.id,
            'cover':drink.cover,
            'name': drink.name,
            'percentage': drink.percentage,
            'breweries': drink.breweries,
            'price':drink.price
    }
    return jsonify(drink_data)

# POST drinks

@app.route('/drinks', methods=['POST'])
def create_drinks():
    data = request.get_json()
    
    rest_drink = Drink(
        name=data['name'],
        cover=data['cover'],
        percentage=data['percentage'],
        breweries=data['breweries'],
        price=data['price']
    )

    db.session.add(rest_drink)
    db.session.commit()

    response = make_response(jsonify({"message": "successfully added"}), 201)
    return response

# UPDATE/PATCH drinks/id
@app.route('/drinks/<int:id>', methods=['PATCH'])
def update_drink(id):
    drink = Drink.query.filter_by(id=id).first()
    
    if not drink:
        return jsonify({'error': 'Drink not found'}), 404
    
    data = request.get_json()
    
    # Update the drink attributes based on the provided data
    if 'name' in data:
        drink.name = data['name']
    if 'cover' in data:
        drink.cover = data['cover']
    if 'percentage' in data:
        drink.percentage = data['percentage']
    if 'breweries' in data:
        drink.breweries = data['breweries']
    if 'price' in data:
        drink.price = data['price']
    
    db.session.commit()
    
    return jsonify({'message': 'Drink updated successfully'})


# DELETE drinks/:id
@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.filter_by(id=id).first()
    if drink:
        db.session.delete(drink)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Drink not found'}), 404
    
# GET customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    customers_list = []
    for customer in customers:
        customers_data = {
            'id': customer.id,
            'username':customer.username,
            'email_address': customer.email_address,
            'password': customer.password
           
            
        }
        customers_list.append(customers_data)
    return jsonify(customers_list)

@app.route("/customers/<int:customer_id>", methods=["GET"])
def get_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()

    if not customer:
        return jsonify({}), 404

    customer_data = {
            'id': customer.id,
            'username':customer.username,
            'email_address': customer.email_address,
            'password': customer.password
    }
    return jsonify(customer_data)



# GET reviews
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



if __name__ == '__main__':
    app.run(port=5555)



# from routes import reviews_blueprint
# app.register_blueprint(reviews_blueprint)
