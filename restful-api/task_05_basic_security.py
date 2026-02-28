#!/usr/bin/python3
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# This runs every time a protected route is accessed
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return users[username]
    return None

# handling error
@auth.error_handler
def unauthorized():
    return jsonify({
        "error": "Unauthorized"
    }), 401
    
# Required Endpoint
@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return jsonify({
        "message": "Basic Auth: Access Granted"
    })

if __name__ == '__main__':
    app.run()
