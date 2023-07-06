from app import db, app
from models import  Review, Drink, Customer


# reviews_data = [
#     {
#         "drink_id": 1,
#         "customer_id": 456,
#         "review": "Great drink!"
#     },
#     {
#         "drink_id": 2,
#         "customer_id": 101,
#         "review": "Amazing flavor!"
#     },
#     {
#         "drink_id": 3,
#         "customer_id": 789,
#         "review": "Refreshing and delicious."
#     },
#     {
#         "drink_id": 4,
#         "customer_id": 654,
#         "review": "Not what I expected. Disappointed."
#     },
#     {
#         "drink_id": 5,
#         "customer_id": 987,
#         "review": "Perfect balance of flavors."
#     },
#     {
#         "drink_id": 6,
#         "customer_id": 321,
#         "review": "Lacks depth. Could be better."
#     },
#     {
#         "drink_id": 7,
#         "customer_id": 456,
#         "review": "Absolutely loved it!"
#     },
#     {
#         "drink_id": 8,
#         "customer_id": 123,
#         "review": "Smooth and satisfying."
#     },
#     {
#         "drink_id": 9,
#         "customer_id": 987,
#         "review": "Too sweet for my taste."
#     },
#     {
#         "drink_id": 10,
#         "customer_id": 101,
#         "review": "Will definitely order again."
#     }
# ]
# drinks_data = [
#     {
#         "id": 1,
#         "cover":"https://cdnprod.mafretailproxy.com/sys-master-root/hea/h34/26759815069726/138548_main.jpg_480Wx480H",
#         "name": "Chrome gin",
#         "percentage": "40%",
#         "breweries":"Keroche breweries",
#         "price": "750"
#     },
#     {
#         "id": 2,
#         "cover":"https://cdnprod.mafretailproxy.com/sys-master-root/ha9/hcc/12463260434462/41955_Main.jpg_480Wx480H",
#         "name": "Chrome vodka",
#         "percentage": "40%",
#         "breweries":"Keroche breweries",
#         "price": "770"
#     },
#     {
#         "id": 3,
#         "cover":"https://cdnprod.mafretailproxy.com/sys-master-root/h08/h67/17307148156958/11149_main.jpg_480Wx480H",
#         "name": "Hennessy",
#         "percentage": "40%",
#         "breweries":"LVMH, Diageo",
#         "price": "2870"
#     },
#     {
#         "id": 4,
#         "cover":"https://thewinebox.biz/wp-content/uploads/2022/01/captain-morgan-spiced-rum.png",
#         "name": "Captain Morgan",
#         "percentage": "39%",
#         "breweries":"Diageo",
#         "price": "1100" 
#     },
#     {
#         "id": 5,
#         "cover":"https://jayswines.com/wp-content/uploads/2022/10/Buy-Best-Whisky-750ml-online-in-Nairobi.jpg",
#         "name": "Best Gin",
#         "percentage": "39%",
#         "breweries":"Oaks & Corks",
#         "price": "800"
#     },
#     {
#         "id": 6,
#         "cover":"data:image/jpeg;base64,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",
#         "name": "Kibao",
#         "percentage": "38%",
#         "breweries":"Kenya Wine Agencies Limited",
#         "price": "700"
#     },
#     {
#         "id": 7,
#         "cover":"https://londondistillers.com/wp-content/uploads/2021/12/general-meakins-spirit-london-distillers-648x648.jpg",
#         "name": "General Meakins",
#         "percentage": "50%",
#         "breweries":"London Distillers Limited",
#         "price": "850"
#     },
#     {
#         "id": 8,
#         "cover":"data:image/jpeg;base64,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",
#         "name": "Konyagi",
#         "percentage": "41%",
#         "breweries":"Nile Breweries Limited",
#         "price": "700"
#     },
#     {
#          "id": 9,
#          "cover":"https://www.oaks.delivery/wp-content/uploads/black-and-white-1l-copy.jpg",
#         "name": "Black and White",
#         "percentage": "40%",
#         "breweries":"Diageo",
#         "price": "1600"
#     },
#     {
#         "id": 10,
#         "cover":"https://storage.googleapis.com/drinksvine/products/johnnie-walker-red-label.webp",
#         "name": "Red Label",
#         "percentage": "40%",
#         "breweries":"Unilever",
#         "price": "2250"
#     }
# ]

# with app.app_context():
#     db.create_all()

#     reviews = []
#     for review_data in reviews_data:
#         review = Review(**review_data)
#         reviews.append(review)
#     db.session.add_all(reviews)
#     db.session.commit()

#     drinks = []
#     for drink_data in drinks_data:
#         drink = Drink(**drink_data)
#         drinks.append(drink)
#     db.session.add_all(drinks)
#     db.session.commit()


# from faker import Faker
# import random
# import json

# fake = Faker()

# sales = []
# for _ in range(10):
#     sale = {
#         'customer_id': random.randint(1, 10),
#         'drink_id': random.randint(1, 10)
#     }
#     sales.append(sale)

# sales_json = json.dumps(sales, indent=4)
# print(sales_json)

from faker import Faker
import bcrypt

fake = Faker()

# Generate 10 faker instances for registration
with app.app_context():
  for i in range(10):
    username = fake.name()
    password = fake.password()
    email_address = fake.email()

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Create and save the customer
    customer = Customer(username=username, password=hashed_password, email_address=email_address)
    db.session.add(customer)
    db.session.commit()


