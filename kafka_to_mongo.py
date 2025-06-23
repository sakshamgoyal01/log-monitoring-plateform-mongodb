from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer(
    'logs-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

mongo = MongoClient("mongodb://localhost:27017/")
db = mongo["ai_logs"]
logs_collection = db["logs"]

for message in consumer:
    log = message.value
    print("Inserting log:", log)
    logs_collection.insert_one(log)
