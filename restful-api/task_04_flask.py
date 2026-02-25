#!/usr/bin/python3
""""command to launch a virtual env for flask
py -m venv .venv
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
    "mary": {"username": "mary", "name": "Mary", "age": 24, "city": "Melbourne"},
    "felix": {"username": "felix", "name": "Felix", "age": 42, "city": "Sydney"}
    }
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=["GET"])
def get_data():
    usernames = []
    for details in users.values():
        usernames.append(details["username"])  
    return jsonify(usernames)

@app.route('/status')
def get_status():
    return 'OK'

@app.route('/users/<string:username>', methods=["GET"])
def get_user_by_username(username):
        user_data = users.get(username)
        if user_data:
             return jsonify(user_data)
        else:
             return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=["POST"])
def add_user():
     data = request


if __name__ == "__main__":
    app.run(debug=True)
