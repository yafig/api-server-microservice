from flask import Flask, request, jsonify, Response
from flask_cors import CORS, cross_origin
from flask_injector import FlaskInjector
from injector import inject
from dependencies import configure
import jwt
from repository.user_model import User
from service.user_service_interface import UserServiceInterface, SECRET_KEY

import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)
app.debug = True

@app.route('/healthz')
def healthz():
    return "OK"

@app.route('/users/login', methods=["POST", "GET"])
@cross_origin()
def login(service: UserServiceInterface) -> Response:
    if request.method == "GET":
        # NuxtJS Authentication requires a user information after successfully logged in to the system
        # Strip 'Bearer: ' in "Bearer {token}" header
        token = request.headers.get("Authorization")[7:]
        payload = jwt.decode(token, SECRET_KEY, algorithms="HS256")
        return jsonify({"username": payload['username']})

    elif request.method == "POST":
        post_data = request.get_json()
        username = post_data['username']
        raw_password = post_data['password']
        token = service.login(username, raw_password)
        return jsonify({"token": token})

@inject
@app.route('/users/register', methods=["POST"])
@cross_origin()
def register(service: UserServiceInterface) -> Response:
    post_data = request.get_json()
    username = post_data['username']
    email = post_data['email']
    password = post_data['password']
    user = service.register(email, username, password)
    return jsonify(user.to_dict())

@inject
@app.route('/users/<string:username>', methods=["GET"])
def get_user(username, service: UserServiceInterface) -> Response:
    user = service.get_user(user_id)
    return jsonify(user.to_dict())

@inject
@app.route('/users/<string:username>', methods=["DELETE"])
def delete_user(username, service: UserServiceInterface) -> Response:
    service.delete_user(username)
    return jsonify({"status": "OK"})

@inject
@app.route('/users/<string:username>', methods=["PUT"])
def edit_user(username, service: UserServiceInterface) -> Response:
    return "OK"

@inject
@app.route('/users/follow/<string:username>', methods=["GET"])
def user_follow(username, service: UserServiceInterface) -> Response:
    return "OK"

@inject
@app.route('/users/block/<string:username>', methods=["GET"])
def user_block(username, service: UserServiceInterface) -> Response:
    return "OK"

@inject
@app.route('/users/<string:username>/posts', methods=["GET"])
def get_user_posts(username, service: UserServiceInterface) -> Response:
    return "OK"

FlaskInjector(app=app, modules=[configure])
