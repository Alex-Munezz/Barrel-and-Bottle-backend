from flask import Flask, jsonify
from flask_migrate import Migrate
from models import Drink, Review, Customer,Sale,db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)
















if __name__ == "__main__":
    app.run(port=5555)
