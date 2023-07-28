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


    def to_dict(self):
        return {
            'id': self.id,
            'cover': self.cover,
            'name': self.name,
            'percentage': self.percentage,
            'breweries': self.breweries,
            'price': self.price
        }

    reviews = db.relationship('Review',cascade='all, delete', backref='drink')
    sales = db.relationship('Sale', backref='drink')



class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"))
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    review = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'drink_id': self.drink_id,
            'customer_id': self.customer_id,
            'review': self.review
        }



class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email_address = db.Column(db.String)
    password = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email_address': self.email_address,
            # 'password': self.password.encode('utf-8')
        }

    reviews = db.relationship('Review',cascade='all, delete', backref='customer')
    sales = db.relationship('Sale', backref='customer')



class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }



class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    drink_id = db.Column(db.Integer, db.ForeignKey("drinks.id"))

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'drink_id': self.drink_id
        }



