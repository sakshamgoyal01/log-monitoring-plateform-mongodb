from kafka import KafkaProducer
from faker import Faker
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

fake = Faker()

services = ['auth', 'payment', 'frontend', 'database']
levels = ['info', 'warn', 'error']

while True:
    log = {
        "service": random.choice(services),
        "level": random.choice(levels),
        "message": fake.sentence(),
        "timestamp": fake.iso8601(),
        "userId": fake.user_name()
    }
    producer.send('logs-topic', log)
    print(f"Sent log: {log}")
    time.sleep(1)
