REST API Conceptual Diagram:
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
Components:

Client: The requester of the service, often a web browser or application.
Web Server: Handles the incoming request, acts as a middleman before passing it to the API server.
API Server: The actual logic layer that processes the request, determining what data or action is required.
Database: Stores the data which the API might fetch or modify.
Flow:

The client sends an HTTP/HTTPS request to the Web Server.
The Web Server, after potential routing and load balancing, forwards the request to the API Server.
The API Server processes the request, interacts with the database if needed.
The API Server returns the processed response to the Web Server.
The Web Server sends back the final HTTP/HTTPS response to the client.