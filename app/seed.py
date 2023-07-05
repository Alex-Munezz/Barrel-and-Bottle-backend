from app import db, app
from models import  Review, Drink


reviews_data = [
    {
        "drink_id": 1,
        "customer_id": 456,
        "review": "Great drink!"
    },
    {
        "drink_id": 2,
        "customer_id": 101,
        "review": "Amazing flavor!"
    },
    {
        "drink_id": 3,
        "customer_id": 789,
        "review": "Refreshing and delicious."
    },
    {
        "drink_id": 4,
        "customer_id": 654,
        "review": "Not what I expected. Disappointed."
    },
    {
        "drink_id": 5,
        "customer_id": 987,
        "review": "Perfect balance of flavors."
    },
    {
        "drink_id": 6,
        "customer_id": 321,
        "review": "Lacks depth. Could be better."
    },
    {
        "drink_id": 7,
        "customer_id": 456,
        "review": "Absolutely loved it!"
    },
    {
        "drink_id": 8,
        "customer_id": 123,
        "review": "Smooth and satisfying."
    },
    {
        "drink_id": 9,
        "customer_id": 987,
        "review": "Too sweet for my taste."
    },
    {
        "drink_id": 10,
        "customer_id": 101,
        "review": "Will definitely order again."
    }
]
drinks_data = [
    {
        "id": 1,
        "name": "Chrome gin",
        "percentage": "40%",
        "breweries":"Keroche breweries",
        "price": "750"
    },
    {
        "id": 2,
        "name": "Chrome vodka",
        "percentage": "40%",
        "breweries":"Keroche breweries",
        "price": "770"
    },
    {
        "id": 3,
        "name": "Hennessy",
        "percentage": "40%",
        "breweries":"LVMH, Diageo",
        "price": "2870"
    },
    {
        "id": 4,
        "name": "Captain Morgan",
        "percentage": "3.5%",
        "breweries":"Diageo",
        "price": "1100" 
    },
    {
        "id": 5,
        "name": "Best Gin",
        "percentage": "39%",
        "breweries":"Oaks & Corks",
        "price": "800"
    },
    {
        "id": 6,
        "name": "Kibao",
        "percentage": "38%",
        "breweries":"Kenya Wine Agencies Limited",
        "price": "700"
    },
    {
        "id": 7,
        "name": "General Meakins",
        "percentage": "50%",
        "breweries":"London Distillers Limited",
        "price": "850"
    },
    {
        "id": 8,
        "name": "Konyagi",
        "percentage": "41%",
        "breweries":"Nile Breweries Limited",
        "price": "700"
    },
    {
         "id": 9,
        "name": "Black and White",
        "percentage": "40%",
        "breweries":"Diageo",
        "price": "1600"
    },
    {
        "id": 10,
        "name": "Red Label",
        "percentage": "40%",
        "breweries":"Unilever",
        "price": "2250"
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

    drinks = []
    for drink_data in drinks_data:
        drink = Drink(**drink_data)
        drinks.append(drink)
    db.session.add_all(drinks)
    db.session.commit()
