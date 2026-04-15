from flask import Blueprint, jsonify, request
from .models import Food, Order
from .db import db

main = Blueprint('main', __name__)

# Home
@main.route('/')
def home():
    return "Welcome to the Food App!"

# Add food (for testing)
@main.route('/add-food', methods=['POST'])
def add_food():
    data = request.json
    food = Food(name=data['name'], price=data['price'])
    db.session.add(food)
    db.session.commit()

    return jsonify({"message": "Food added"})

# Get all food
@main.route('/foods')
def get_foods():
    foods = Food.query.all()
    result = []

    for f in foods:
        result.append({
            "id": f.id,
            "name": f.name,
            "price": f.price
        })

    return jsonify(result)

# Place order
@main.route('/order', methods=['POST'])
def order():
    data = request.json
    new_order = Order(food_name=data['food_name'])

    db.session.add(new_order)
    db.session.commit()

    return jsonify({"message": "Order placed"})