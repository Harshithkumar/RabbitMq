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


## Setup

1. **Clone the Repository**

   ```sh
   git clone <repository_url>
   cd <repository_directory>

## Usage
1. Start the Services
   Start RabbitMQ, producer, and consumer services using Docker Compose:
   ```sh
   _docker-compose up -d_
3. Access RabbitMQ Management Interface
   ```sh
   _Username: guest
   Password: guest_
5. Check Logs
   ```sh
   _docker-compose logs -f producer
   docker-compose logs -f consumer_

## Dependencies
    ```sh
    pip install -r requirements.txt

## Cleaning Up
    ```sh
    docker-compose down

## Acknowledgments
   Pika Library
   RabbitMQ
   Docker
