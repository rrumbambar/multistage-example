# Multi-Stage Example

This is a simple Python app with two containers: a **server** and a **client** that demonstrates communication between 2 containers and example of multistage build. The server provides an endpoint, and the client communicates with the server to fetch data.

## Features
- **Server**: A Flask-based API exposing a `/greeting` endpoint.
- **Client**: A Python script making HTTP requests to the server.

## Build and Run
- `docker compose build`
- `docker compose up`
- The client will automatically make a request to the server and display the response in the logs: `{'message': 'Hi Client!'}`

## Docker images
-  https://hub.docker.com/r/dbatruh/multistage-example/tags

