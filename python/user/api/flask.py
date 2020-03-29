from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from flask_injector import FlaskInjector
from injector import inject
from dependencies import configure

from repository.user_model import User
from service.user_service_interface import UserServiceInterface

import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
app.debug = True
SECRET_KEY = "random string"

@app.route('/healthz')
def healthz():
    return "OK"

@app.route('/users/login', methods=["POST", "GET"])
@cross_origin()
def login(service: UserServiceInterface):
    if request.method == "GET":
        # NuxtJS Authentication requires a user information after successfully logged in to the system
        # Strip 'Bearer: ' in "Bearer {token}" header
        token = request.headers.get("Authorization")[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return jsonify({"username": payload['username']})

    elif request.method == "POST":
        post_data = request.get_json()
        if user := User.query.filter(User.email == post_data['email']).first():
            if hash_password(post_data['password'], user.password_salt).decode() == user.password:
                payload = {"username": user.username, "fullname": user.fullname, "status": user.status}
                token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
                return jsonify({"token": token.decode()})

            return jsonify({"error_message": "Username & password is not matched"}), 403
        else:
            return jsonify({"error_message": "User does not exist"}), 403

@inject
@app.route('/users/register', methods=["POST"])
@cross_origin()
def register(service: UserServiceInterface):
    post_data = request.get_json()
    username = post_data['username']
    email = post_data['email']
    password = post_data['password']

    service.register(email, username, password)
    return jsonify({"status": "OK"})

@inject
@app.route('/users/<string:user_id>', methods=["GET"])
def get_user(user_id, service: UserServiceInterface):
    return jsonify(service.get_user(user_id).to_dict())

@app.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id, service: UserServiceInterface):
    return "OK"

@app.route('/users/<user_id>', methods=["PUT"])
def edit_user(user_id, service: UserServiceInterface):
    return "OK"

@app.route('/users/follow/<user_id>', methods=["GET"])
def user_follow(user_id, service: UserServiceInterface):
    return "OK"

@app.route('/users/block/<user_id>', methods=["GET"])
def user_block(user_id, service: UserServiceInterface):
    return "OK"

@app.route('/users/<user_id>/posts', methods=["GET"])
def get_user_posts(user_id, service: UserServiceInterface):
    return "OK"

FlaskInjector(app=app, modules=[configure])
