import pika
import uuid
import time
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_rabbitmq_connection():
    parameters = pika.ConnectionParameters('rabbitmq')
    retries = 5
    for i in range(retries):
        try:
            return pika.BlockingConnection(parameters)
        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"Connection failed, retrying in 5 seconds ({i+1}/{retries})...")
            time.sleep(5)
    raise Exception("Failed to connect to RabbitMQ after several attempts")

def produce_message():
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue='test_queue')

    while True:
        message = {
            "message_id": str(uuid.uuid4()),
            "created_on": datetime.now().isoformat()
        }
        message_body = json.dumps(message)
        channel.basic_publish(exchange='',
                              routing_key='test_queue',
                              body=message_body)
        logging.info(f"Sent: {message_body}")
        time.sleep(5)

if __name__ == "__main__":
    produce_message()
