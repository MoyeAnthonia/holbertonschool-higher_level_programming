#!/usr/bin/python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)

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

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username in users and check_password_hash(users[username]["password"],
                                                 password):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token)

    return jsonify({"msg": "Bad credentials"}), 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    if not current_user:
        return jsonify({"message": "Unauthorized"}), 401
    return jsonify("JWT Auth: Access Granted"), 200

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token(err):
    return jsonify({"error": "Fresh token required"}), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200

if __name__ == '__main__':
    app.run()
