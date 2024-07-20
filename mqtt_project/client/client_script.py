import pika
import time
import random
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='mqtt', exchange_type='topic')

def emit_message():
    while True:
        status = random.randint(0, 6)
        message = json.dumps({'status': status})
        channel.basic_publish(exchange='mqtt', routing_key='status', body=message)
        print(f" [x] Sent {message}")
        time.sleep(1)

try:
    emit_message()
except KeyboardInterrupt:
    connection.close()
