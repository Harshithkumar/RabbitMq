# RabbitMQ Producer and Consumer

This project demonstrates a simple setup of a RabbitMQ producer and consumer using Docker and Python. The producer sends messages to RabbitMQ, and the consumer receives these messages. The messages contain a UUID and a timestamp.

## Requirements

- Docker
- Docker Compose
- Python 3.8+

## Project Structure
.
├── docker-compose.yml
├── producer.py
├── consumer.py
├── Dockerfile
├── requirements.txt
└── README.md


## Setup

1. **Clone the Repository**

   ```sh
   git clone <repository_url>
   cd <repository_directory>

## Usage
1. Start the Services
   Start RabbitMQ, producer, and consumer services using Docker Compose:
   _docker-compose up -d_
2. Access RabbitMQ Management Interface
   _Username: guest
   Password: guest_
3. Check Logs
   _docker-compose logs -f producer
   docker-compose logs -f consumer_

## Dependencies
pip install -r requirements.txt

## Cleaning Up
docker-compose down

## Acknowledgments
   Pika Library
   RabbitMQ
   Docker
