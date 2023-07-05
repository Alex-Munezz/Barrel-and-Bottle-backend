# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey
# from sqlalchemy.orm import relationship


# db = SQLAlchemy()

# def create_all_tables():
#     from app import app
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()

# from app import db

# class Drink(db.Model):
#     __tablename__ = 'drinks'
#     id = db.Column(db.Integer, primary_key=True)
#     
#     name = db.Column(db.String, unique=True)
#     percentage = db.Column(db.Integer)
#     breweries = db.Column(db.String)
#     price = db.Column(db.Integer)

#     reviews = db.relationship('Review', backref='drink', lazy='dynamic')
#     sales = db.relationship('Sale', backref='drink', cascade='all, delete-orphan')

#     def __init__(self, id, cover, name, percentage, breweries, price):
#         self.id = id
#         self.cover = cover
#         self.name = name
#         self.percentage = percentage
#         self.breweries = breweries
#         self.price = price


# class Review(db.Model):
#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer, primary_key=True)
#     drink_id = db.Column(db.Integer, db.ForeignKey('drinks.id'), nullable=False)
#     # drink_id = db.Column(db.Integer, nullable=False)
#     customer_id = db.Column(db.Integer, ForeignKey('customers.id'))
#     review = db.Column(db.String(255), nullable=False)

#     # drink_id = db.Column(db.Integer, ForeignKey('drinks.id'), nullable=False)
#     def __init__(self, drink_id, customer_id, review):
#         self.drink_id = drink_id
#         self.customer_id = customer_id
#         self.review = review
    


# class Customer(db.Model):
#     __tablename__ = 'customers'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String)
#     email_address = db.Column(db.String)
#     password = db.Column(db.String)

#     reviews = relationship('Review', backref='customer')
#     sales = db.relationship('Sale', backref='customer', cascade='all, delete-orphan')

#     def __init__(self, username, email_address, password):
#         self.username = username
#         self.email_address = email_address
#         self.password = password


# class Admin(db.Model):
#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String)
#     password = db.Column(db.String)

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password


# class Sale(db.Model):
#     __tablename__ = 'sales'
#     id = db.Column(db.Integer, primary_key=True)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
#     drink_id = db.Column(db.Integer, db.ForeignKey('drinks.id'))

#     def __init__(self, customer_id, drink_id):
#         self.customer_id = customer_id
#         self.drink_id = drink_id
















from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Drink(db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    cover = db.Column(db.String(100000), unique=True)
    percentage = db.Column(db.Integer)
    breweries = db.Column(db.String)
    price = db.Column(db.Integer)

    reviews = db.relationship('Review',cascade='all, delete', backref='drink')
    sales = db.relationship('Sale', backref='drink')

    # def __init__(self, name,cover,type, percentage, breweries, price):
    #     self.name = name
    #     self.type = type
    #     self.cover = cover
    #     self.percentage = percentage
    #     self.breweries = breweries
    #     self.price = price


class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    review = db.Column(db.String)

    def __init__(self, review):
        self.review = review


class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email_address = db.Column(db.String)
    password = db.Column(db.String)

    reviews = db.relationship('Review', backref='customer')
    sales = db.relationship('Sale', backref='customer')

    def __init__(self, username, email_address, password):
        self.username = username
        self.email_address = email_address
        self.password = password


class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"))

    def __init__(self, customer_id, drink_id):
        self.customer_id = customer_id
        self.drink_id = drink_id

