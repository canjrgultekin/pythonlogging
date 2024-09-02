
# Flask-Based Microservices with Centralized Logging

This project demonstrates a microservice architecture built with Flask in Python, featuring a centralized logging system using Kafka and Elasticsearch. The architecture consists of three main services—User Service, Hotel Service, and Reservation Service—along with an API Gateway that handles routing and logging.

## Project Structure

```bash
otel_rezervasyon/
├── api_gateway/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── user_service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── user_data.py
├── hotel_service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── hotel_data.py
├── reservation_service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── reservation_data.py
├── common/
│   ├── kafka_service.py
│   ├── elasticsearch_service.py
│   └── database.py
├── docker-compose.yml
└── otel-collector-config.yaml
```

## Features

- **User Service**: Manages user registration and authentication.
- **Hotel Service**: Handles hotel data management.
- **Reservation Service**: Manages hotel reservations.
- **API Gateway**: Routes requests to the appropriate services and logs actions centrally.
- **Centralized Logging**: Uses Kafka to collect logs from all services and Elasticsearch to store and analyze logs.
- **Monitoring and Visualization**: Uses Kibana to visualize logs and monitor system behavior.

## Technologies Used

- **Flask**: Python micro web framework.
- **Kafka**: Distributed messaging system for log aggregation.
- **Elasticsearch**: Search and analytics engine for storing and querying logs.
- **Kibana**: Data visualization tool for Elasticsearch.
- **Docker**: Containerization platform to manage the microservices.

## Getting Started

### Prerequisites

- Docker and Docker Compose installed on your machine.

 Build and start the services using Docker Compose:

   ```bash
   docker-compose up --build
   ```
 Access the services via the API Gateway:

   - User Service: `http://localhost:5003/user/<action>`
   - Hotel Service: `http://localhost:5003/hotel/<action>`
   - Reservation Service: `http://localhost:5003/reservation/<action>`

### Logging and Monitoring

- **Kafka**: Log messages are sent to the `otel-logs` topic.
- **Elasticsearch**: Logs are stored in the `otel-logs` index.
- **Kibana**: Visualize logs at `http://localhost:5601`.

### Example Requests

- **Register a User:**

   ```bash
   curl -X POST http://localhost:5003/user/register -H "Content-Type: application/json" -d '{"username": "john_doe", "password": "secure_password"}'
   ```

- **Login a User:**

   ```bash
   curl -X POST http://localhost:5003/user/login -H "Content-Type: application/json" -d '{"username": "john_doe", "password": "secure_password"}'
   ```
