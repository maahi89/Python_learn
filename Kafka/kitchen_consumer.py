from kafka import KafkaConsumer

import json

from database import SessionLocal
from models import Order

consumer = KafkaConsumer(
    'food_orders_json',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

db = SessionLocal()

print("Kitchen Consumer Running...\n")

for message in consumer:

    data = message.value

    print(f"Preparing {data['food']}")

    new_order = Order(
        customer=data['customer'],
        food=data['food'],
        quantity=data['quantity'],
        status="Preparing"
    )

    db.add(new_order)

    db.commit()