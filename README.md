# RabbitMQ Producer and Consumer

This project demonstrates a simple setup of a RabbitMQ producer and consumer using Docker and Python. The producer sends messages to RabbitMQ, and the consumer receives these messages. The messages contain a UUID and a timestamp.

## Requirements

- Docker
- Docker Compose
- Python 3.8+

## Project Structure
.

|__ docker-compose.yml

|__ producer.py

|__ consumer.py

|__ Dockerfile

|__ requirements.txt

|__ README.md

## Scripts
   Producer:
      The producer.py script sends a message to RabbitMQ every 5 seconds. Each message contains a UUID and a timestamp.

   Consumer:
      The consumer.py script receives messages from RabbitMQ and logs them.

   Dockerfile:
      The Dockerfile sets up the environment for running the producer and consumer scripts.

   Configuration:
      You can configure the message sending interval in producer.py:

      MESSAGE_INTERVAL = 5  # Time in seconds

## Setup
1. **Clone the Repository**

   ```sh
   git clone <repository_url>
   cd <repository_directory>

## Usage
1. Start the Services
   Start RabbitMQ, producer, and consumer services using Docker Compose:
   ```sh
   docker-compose up -d
3. Access RabbitMQ Management Interface
   ```sh
   Username: guest
   Password: guest
5. Check Logs
   ```sh
   docker-compose logs -f producer
   docker-compose logs -f consumer

## Dependencies
    ```sh
    pip install -r requirements.txt

## Cleaning Up
    ```sh
    docker-compose down

## Acknowledgments
   1. Pika Library
   2. RabbitMQ
   3. Docker
