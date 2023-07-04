from faker import Faker
from models import Drink, Review, Customer, Sale, db
from main import app
import random

fake = Faker()

with app.app_context():
    drinks = []
    for i in range(10):
        result = Drink(
            name=fake.name(),
            percentage=fake.text(),
            breweries=fake.company(),  # Use 'company()' instead of 'breweries()'
            price=fake.currency()
        )
        drinks.append(result)

    db.session.add_all(drinks)
    db.session.commit()

    reviews = []
    for i in range(10):
        result = Review(
            id=fake.random_int(),
            drink_id=fake.drink_id(),
            customer_id=fake.int(),
            review=fake.review()
        )
        reviews.append(result)

    db.session.add_all(reviews)
    db.session.commit()



# # from flask_sqlalchemy import SQLAlchemy
# from faker import Faker
# from models import Drink, Review, Customer,Sale,db
# from main import app

# fake = Faker()

# with app.app_context():


#     drinks = []
#     for i in range(10):
#         result = Drink(id = fake.random_int(),name=fake.name(),percentage=fake.text(),breweries=fake.breweries(),price=fake.price())
#         drinks.append(result)

#     db.session.add_all(drinks)
#     db.session.commit()

#     reviews = []
#     for i in range(10):
#         result = Review(id = fake.random_int(),drink_id=fake.drink_id(),customer_id=fake.int(),review=fake.review())
#         reviews.append(result)

#     db.session.add_all(reviews)
#     db.session.commit()






























# from faker import Faker
# from flask_sqlalchemy import SQLAlchemy
# from models import Drink, Review, Customer,Sale
# from main import app

# db = SQLAlchemy()
# fake = Faker()


# with app.app_context():
#     drink =[]

#     # Generate fake drinks
#     for _ in range(10):
#         drink = Drink(
#             name=fake.word(),
#             type=fake.word(),
#             percentage=fake.random_int(min=1, max=100),
#             breweries=fake.word(),
#             price=fake.random_int(min=1, max=100)
#         )
#         db.session.add(drink)

#     # Generate fake customers
# #     for _ in range(10):
# #         customer = Customer(
# #             username=fake.user_name(),
# #             email_address=fake.email(),
# #             password=fake.password()
# #         )
# #         db.session.add(customer)

# #     # Generate fake reviews
# #     drinks = Drink.query.all()
# #     customers = Customer.query.all()
# #     for _ in range(20):
# #         drink = fake.random_element(drinks)
# #         customer = fake.random_element(customers)
# #         review = Review(
# #             drink_id=drink.id,
# #             customer_id=customer.id,
# #             review=fake.paragraph()
# #         )
# #         db.session.add(review)

# #     # Generate fake sales
# #     for _ in range(50):
# #         drink = fake.random_element(drinks)
# #         customer = fake.random_element(customers)
# #         sale = Sale(
# #             customer_id=customer.id,
# #             drink_id=drink.id
# #         )
# #         db.session.add(sale)

# #     db.session.commit()


# Usage
# create_fake_data()
