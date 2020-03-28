from flask import Flask, request, jsonify
import jwt
from repository.models import db, User
from flask_cors import CORS, cross_origin
import os
from helper import hash_password, randomString

MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME", "root")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "password")
MYSQL_HOST =  os.environ.get("MYSQL_HOST", "mysql")
MYSQL_TABLE = os.environ.get("MYSQL_TABLE", "yafig")
MYSQL_URI = f"mysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_TABLE}"

def create_app(config_name="PRODUCTION"):
    app = Flask(__name__)
    if config_name == "PRODUCTION":
        app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_URI

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    return app

app = create_app("PRODUCTION")
CORS(app)
app.debug = True
SECRET_KEY = "random string"

@app.route('/healthz')
def healthz():
    return "OK"

@app.route('/users/login', methods=["POST", "GET"])
@cross_origin()
def login():
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

@app.route('/users/register', methods=["POST"])
@cross_origin()
def register():
    post_data = request.get_json()

    # Check if the username already exist
    if User.query.filter(User.email == post_data['email']).count():
        return jsonify({"error_message": "Email is already registered"}), 403

    if User.query.filter(User.username == post_data['username']).count():
        return jsonify({"error_message": "Username is already taken"}), 403

    salt = randomString(32)
    hashed_password = hash_password(post_data['password'], salt)
    new_user = User(username=post_data['username'], email=post_data['email'], password=hashed_password, password_salt=salt)

    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        db.session.rollback()

    return jsonify({"status": "OK"})

@app.route('/users/<user_id>', methods=["GET"])
def get_user(user_id):
    return "OK"

@app.route('/users/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    return "OK"

@app.route('/users/<user_id>', methods=["PUT"])
def edit_user(user_id):
    return "OK"

@app.route('/users/follow/<user_id>', methods=["GET"])
def user_follow(user_id):
    return "OK"

@app.route('/users/block/<user_id>', methods=["GET"])
def user_block(user_id):
    return "OK"

@app.route('/users/<user_id>/posts', methods=["GET"])
def get_user_posts(user_id):
    return "OK"
