from kafka import KafkaProducer
import time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

orders = [
    "Pizza",
    "Burger",
    "Chicken Biryani",
    "Fried Rice"
]

for order in orders:

    producer.send(
        'food_orders',
        order.encode('utf-8')
    )

    print(f"Order Sent: {order}")

    time.sleep(2)

producer.flush()