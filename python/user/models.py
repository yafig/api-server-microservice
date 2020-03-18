from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    email = db.Column(db.String(256))
    fullname = db.Column(db.String(64))
    password = db.Column(db.String(256))
    password_salt = db.Column(db.String(32))
    status = db.Column(db.String(64))
