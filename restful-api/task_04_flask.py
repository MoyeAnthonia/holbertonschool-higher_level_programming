#!/usr/bin/python3
""""command to launch a virtual env for flask
py -m venv .venv
"""
from flask import Flask, jsonify

app = Flask(__name__)
users = [{
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}
    }]
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=["GET"])
def get_data():
    return jsonify({"users": users})

if __name__ == "__main__":
    app.run(debug=True)
