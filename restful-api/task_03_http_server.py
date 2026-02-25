#!/usr/bin/python3
"""setting up http.server"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


PORT = 8000
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Get the http response"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            response_message = b"OK"
            self.wfile.write(response_message)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, MyRequestHandler)
    print(f"Server started on http://localhost:{PORT}")
    httpd.serve_forever()
    httpd.server_close()
    print("Server is closed")

if __name__ == "__main__":
    run()
