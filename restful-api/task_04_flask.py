#!/usr/bin/python3
""""command to launch a virtual env for flask
py -m venv .venv
"""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}
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
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    try:
        new_user = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not new_user:
        return jsonify({"error": "Invalid JSON"}), 400

    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
