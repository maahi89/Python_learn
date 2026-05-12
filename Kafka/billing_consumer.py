from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'food_orders_json',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Billing Consumer Running...\n")

for message in consumer:

    data = message.value

    print(
        f"Generating bill for {data['customer']}"
    )