# MQTT Client-Server Project

This project demonstrates a client-server architecture using MQTT messages via RabbitMQ. The client emits MQTT messages containing random status values, and the server processes these messages, storing them in MongoDB. The server also provides an endpoint to retrieve the count of each status within a specified time range.

## Project Structure

mqtt_project/
├── client/
│ └── client_app.py
├── server/
│ └── server_app.py
├── api/
│ └── flask_app.py
├── requirements.txt
├── README.md

## Workflow
### Client:

The client emits MQTT messages every second.
Each message contains a random status value between 0 and 6.
The message is published to RabbitMQ.

### Server:

The server listens for incoming MQTT messages from RabbitMQ.
Each message is processed, and a timestamp is added.
The message is then stored in MongoDB.

### API:

The API provides an endpoint to retrieve the count of each status within a specified time range.
A query is made to MongoDB using the provided start and end timestamps.
The count of each status is aggregated and returned as a JSON response.


## Setup

1. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

2. **Run the Scripts**
    ```bash
    python api/app.py
    python server/server_script.py
    python client/client_script.py
## Diagram
                          +-------------------+
                          |   Client Script   |
                          +-------------------+
                                  |
                                  | Publishes MQTT messages
                                  v
                          +-------------------+
                          |   RabbitMQ        |
                          +-------------------+
                                  |
                                  | Consumes MQTT messages
                                  v
                          +-------------------+
                          |   Server Script   |
                          +-------------------+
                                  |
                                  | Stores messages in MongoDB
                                  v
                          +-------------------+
                          |   MongoDB         |
                          +-------------------+
                                  |
                                  | Retrieves counts from MongoDB
                                  v
                          +-------------------+
                          |   API (Flask)     |
                          +-------------------+
                                  |
                                  | Responds with status counts
                                  v
                      +-------------------------------+
                      |   Client (Postman/Browser)    |
                      +-------------------------------+
## Example Request

    GET http://127.0.0.1:5000/status_count?start=START_TIMESTAMP&end=END_TIMESTAMP
### Example
    
    GET http://127.0.0.1:5000/status_count?start=1721433676&end=1721433678

## Note
- Ensure RabbitMQ and MongoDB are running before starting the applications.
- Replace START_TIMESTAMP and END_TIMESTAMP with valid Unix timestamps when querying the status count endpoint.