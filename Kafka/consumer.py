from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'food_orders',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

print("Waiting for food orders...\n")

for message in consumer:

    order = message.value.decode('utf-8')

    print(f"Preparing: {order}")