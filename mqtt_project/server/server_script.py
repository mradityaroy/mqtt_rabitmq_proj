import pika
import json
import time
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.mqtt
collection = db.messages

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='mqtt', exchange_type='topic')

result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='mqtt', queue=queue_name, routing_key='status')

def callback(ch, method, properties, body):
    message = json.loads(body)
    message['timestamp'] = time.time()
    collection.insert_one(message)
    print(f" [x] Received {message}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
