import pika
import json
import logging
import time

# Configure logging
logging.basicConfig(level=logging.INFO)


def get_rabbitmq_connection():
    parameters = pika.ConnectionParameters('rabbitmq')
    retries = 5
    for i in range(retries):
        try:
            return pika.BlockingConnection(parameters)
        except pika.exceptions.AMQPConnectionError as e:
            logging.error(f"Connection failed, retrying in 5 seconds ({i + 1}/{retries})...")
            time.sleep(5)
    raise Exception("Failed to connect to RabbitMQ after several attempts")


def callback(ch, method, properties, body):
    message = json.loads(body)
    logging.info(f"Received: {message}")


def consume_message():
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue='test_queue')
    channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)

    logging.info('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    consume_message()
