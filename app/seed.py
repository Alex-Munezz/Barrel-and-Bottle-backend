from main import db, app
from models import Review


reviews_data = [
    {
        "drink_id": 123,
        "customer_id": 456,
        "review": "Great drink!"
    },
    {
        "drink_id": 789,
        "customer_id": 101,
        "review": "Amazing flavor!"
    },
    {
        "drink_id": 456,
        "customer_id": 789,
        "review": "Refreshing and delicious."
    },
    {
        "drink_id": 987,
        "customer_id": 654,
        "review": "Not what I expected. Disappointed."
    },
    {
        "drink_id": 321,
        "customer_id": 987,
        "review": "Perfect balance of flavors."
    },
    {
        "drink_id": 654,
        "customer_id": 321,
        "review": "Lacks depth. Could be better."
    },
    {
        "drink_id": 789,
        "customer_id": 456,
        "review": "Absolutely loved it!"
    },
    {
        "drink_id": 101,
        "customer_id": 123,
        "review": "Smooth and satisfying."
    },
    {
        "drink_id": 654,
        "customer_id": 987,
        "review": "Too sweet for my taste."
    },
    {
        "drink_id": 456,
        "customer_id": 101,
        "review": "Will definitely order again."
    }
]


with app.app_context():
    db.create_all()

    reviews = []
    for review_data in reviews_data:
        review = Review(**review_data)
        reviews.append(review)
    db.session.add_all(reviews)
    db.session.commit()
# import random

# fake = Faker()

# with app.app_context():
#     from faker import Faker
# import random

# fake = Faker()

# # Create and seed database objects
# drinks = [
#     Drink(
#         name=fake.name(),
#         percentage=random.randint(1, 10),
#         breweries=fake.company(),
#         price=(fake.currency_code(), fake.currency_name())
#     )
#     for _ in range(10)
# ]

# reviews = [
#     Review(
#         comment=fake.sentence(),
#         rating=random.randint(1, 5),
#         drink_id=random.choice(drinks).id,
#         customer_id=random.randint(1, 100)
#     )
#     for _ in range(20)
# ]

# # Add objects to the session
# db.session.add_all(drinks)
# db.session.add_all(reviews)

# # Commit the session to persist the objects in the database
# db.session.commit()



    
    # drinks = []
    # for i in range(10):
    #     result = Drink(
    #         # id=random.randint(1,9),
    #         name=fake.name(),
    #         percentage=random.randint(1,9),
    #         breweries=fake.company(),  # Use 'company()' instead of 'breweries()'
    #         price=random.randint(1,9)
    #     )
    #     drinks.append(result)

    # db.session.add_all(drinks)
    # db.session.commit()

    # reviews = []
    # for i in range(10):
    #     result = Review(
    #         # id=random.randint(1,5),
    #         # drink_id=random.randint(1,4),
    #         # customer_id=random.randint(1,3),
    #         review=fake.word()
    #     )
    #     reviews.append(result)

    # db.session.add_all(reviews)
    # db.session.commit()



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
