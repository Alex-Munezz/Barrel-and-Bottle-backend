from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
import os
import bcrypt

from flask_migrate import Migrate
from models import db, Review,Drink, Customer,Admin, Sale
app = Flask(__name__)
# secret_key = os.urandom(32)
# secret_key_string = secret_key.hex()
app.secret_key = "1723afcb0375f79f516ba7455d2940bd12dbe0a4364ba89b4e755bb8a2953a37"

# print(secret_key_string)

CORS(app)
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
    drinks_list = [drink.to_dict() for drink in drinks]
    return jsonify(drinks_list)


@app.route('/drinks/<int:drink_id>', methods=['GET'])
def get_drink(drink_id):
    drink = Drink.query.get(drink_id)

    if not drink:
        return jsonify({'error': 'Drink not found'}), 404

    drink_data = drink.to_dict()
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
    customers_list = [customer.to_dict() for customer in customers]
    return jsonify(customers_list)


@app.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if not customer:
        return jsonify({'error': 'Customer not found'}), 404

    customer_data = customer.to_dict()
    return jsonify(customer_data)

# POST customers
@app.route('/customers', methods=['POST'])
def create_customers():
    data = request.get_json()
    
    rest_customer = Customer(
        username=data['username'],
        email_address=data['email_address'],
        password=data['password']
    )

    db.session.add(rest_customer)
    db.session.commit()

    response = make_response(jsonify({"message": "successfully added"}), 201)
    return response

# PATCH customers/id
@app.route('/customers/<int:id>', methods=['PATCH'])
def update_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    
    if not customer:
        return jsonify({'error': 'Customer not found'}), 404
    
    data = request.get_json()
    
    # Update the customer attributes based on the provided data
    if 'username' in data:
        customer.username = data['username']
    if 'email_address' in data:
        customer.email_address = data['email_address']
    if 'password' in data:
        customer.password = data['password']
   
    
    db.session.commit()
    
    return jsonify({'message': 'Customer updated successfully'})

# DELETE customer
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.query.filter_by(id=id).first()
    if customer:
        db.session.delete(customer)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Customer not found'}), 404
    
# GET admin
@app.route('/admins', methods=['GET'])
def get_admins():
    admins = Admin.query.all()
    admins_list = [admin.to_dict() for admin in admins]
    return jsonify(admins_list)

# POST admin
@app.route('/admins', methods=['POST'])
def create_admins():
    data = request.get_json()
    
    rest_admin = Admin(
        username=data['username'],
        password=data['password']
    )

    db.session.add(rest_admin)
    db.session.commit()

    response = make_response(jsonify({"message": "successfully added"}), 201)
    return response

# PATCH/UPDATE admins
@app.route('/admins/<int:id>', methods=['PATCH'])
def update_admin(id):
    admin = Admin.query.filter_by(id=id).first()
    
    if not admin:
        return jsonify({'error': 'Admin not found'}), 404
    
    data = request.get_json()


    if 'username' in data:
        admin.username = data['username']
    if 'password' in data:
        admin.password = data['password']
   
    
    db.session.commit()
    
    return jsonify({'message': 'Admin updated successfully'})

# DELETE admin
@app.route('/admins/<int:id>', methods=['DELETE'])
def delete_admin(id):
    admin = Admin.query.filter_by(id=id).first()
    if admin:
        db.session.delete(admin)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Admin not found'}), 404

# GET sales
@app.route('/sales', methods=['GET'])
def get_sales():
    sales = Sale.query.all()
    sales_list = [sale.to_dict() for sale in sales]
    return jsonify(sales_list)


# POST sales
@app.route('/sales', methods=['POST'])
def create_sales():
    data = request.get_json()
    
    rest_sale = Sale(
        customer_id=data['customer_id'],
        drink_id=data['drink_id']
    )

    db.session.add(rest_sale)
    db.session.commit()

    response = make_response(jsonify({"message": "successfully added"}), 201)
    return response




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


# LOGIN/REGISTER


@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    email_address = request.json.get('email_address')

    # Hashing the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    customer = Customer(username=username, password=hashed_password.encode('utf-8'), email_address=email_address)

    db.session.add(customer)
    db.session.commit()

    return jsonify({'message': 'Customer registered successfully'})


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    customer = authenticate_user(username, password)

    if customer:
        session['customer_id'] = customer.id
        return jsonify({'message': 'Customer logged in successfully'})
    else:
        return jsonify({'message': 'Invalid customer username or password'}), 401

@app.route('/check_session')
def check_session():
    customer_id = session.get('customer_id')
    if customer_id:
        customer = Customer.query.get(customer_id)
        if customer:
            return jsonify({'message': ' Customer session is active', 'customer': customer.username})
        else:
            
            session.pop('customer_id', None)
            return jsonify({'message': 'Customer session is not active'}), 401
    else:
        return jsonify({'message': 'Customer session is not active'}), 401
    
@app.route('/logout')
def logout():
    customer_id = session.get('customer_id')
    if customer_id:
        session.pop('customer_id')
        return jsonify({'message': 'Customer logged out successfully'})
    else:
        return jsonify({'message': 'No active session'}), 401


# Helper function to authenticate the customer
def authenticate_user(username, password):
    customer = Customer.query.filter_by(username=username).first()
    if customer and bcrypt.checkpw(password.encode('utf-8'), customer.password):
        return customer
    return None



if __name__ == '__main__':
    app.run(port=5555)



# # from routes import reviews_blueprint
# app.register_blueprint(reviews_blueprint)


# @app.route('/drinks', methods=['GET'])
# def get_drinks():
#     drinks = Drink.query.all()
#     drinks_list = []
#     for drink in drinks:
#         drinks_data = {
#             'id': drink.id,
#             'cover':drink.cover,
#             'name': drink.name,
#             'percentage': drink.percentage,
#             'breweries': drink.breweries,
#             'price':drink.price
            
#         }
#         drinks_list.append(drinks_data)
#     return jsonify(drinks_list)

# @app.route("/drinks/<int:drink_id>", methods=["GET"])
# def get_drink(drink_id):
#     drink = Drink.query.filter_by(id=drink_id).first()

#     if not drink:
#         return jsonify({}), 404

#     drink_data = {
#             'id': drink.id,
#             'cover':drink.cover,
#             'name': drink.name,
#             'percentage': drink.percentage,
#             'breweries': drink.breweries,
#             'price':drink.price
#     }
#     return jsonify(drink_data)

# @app.route('/customers', methods=['GET'])
# def get_customers():
#     customers = Customer.query.all()
#     customers_list = []
#     for customer in customers:
#         customers_data = {
#             'id': customer.id,
#             'username':customer.username,
#             'email_address': customer.email_address,
#             'password': customer.password
           
            
#         }
#         customers_list.append(customers_data)
#     return jsonify(customers_list)


# @app.route("/customers/<int:customer_id>", methods=["GET"])
# def get_customer(customer_id):
#     customer = Customer.query.filter_by(id=customer_id).first()

#     if not customer:
#         return jsonify({}), 404

#     customer_data = {
#             'id': customer.id,
#             'username':customer.username,
#             'email_address': customer.email_address,
#             'password': customer.password
#     }
#     return jsonify(customer_data)

# @app.route('/admins', methods=['GET'])
# def get_admins():
#     admins = Admin.query.all()
#     admins_list = []
#     for admin in admins:
#         admins_data = {
#             'id': admin.id,
#             'username':admin.username,
#             'password': admin.password
#         }
#         admins_list.append(admins_data)
#     return jsonify(admins_list)

# @app.route('/sales', methods=['GET'])
# def get_sales():
#     sales = Sale.query.all()
#     sales_list = []
#     for sale in sales:
#         sales_data = {
#             'id': sale.id,
#             'customer_id':sale.customer_id,
#             'drink_id': sale.drink_id
#         }
#         sales_list.append(sales_data)
#     return jsonify(sales_list)