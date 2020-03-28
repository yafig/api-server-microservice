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

@inject
@app.route('/users/<user_id>', methods=["GET"])
def get_user(user_id, service: UserServiceInterface):
    return service.get_user("test")

FlaskInjector(app=app, modules=[configure])
