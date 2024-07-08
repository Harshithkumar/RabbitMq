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

   ```
   git clone <repository_url>
   cd <repository_directory>
   ```
2. **Usage**
   Start the Services
   Start RabbitMQ, producer, and consumer services using Docker Compose:
     ```
     docker-compose up -d
     ```
3.  **Access RabbitMQ Management Interface**
    ```
    Username: guest
    Password: guest
    ```
4.  **Check Logs**
     ```
     docker-compose logs -f producer
     docker-compose logs -f consumer
      ```
## Dependencies
   ```
    pip install -r requirements.txt
   ```
## Cleaning Up
```commandline
docker-compose down
```

## Acknowledgments
   1. Pika Library
   2. RabbitMQ
   3. Docker
