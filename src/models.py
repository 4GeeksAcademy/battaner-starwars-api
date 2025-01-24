import os
import sys
from sqlalchemy import ForeignKey, Integer, String
from eralchemy2 import render_er
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, unique = True)
    username = db.Column(db.String(250), nullable=False, unique = True)
    firstname = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique = True)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)

class Media(db.Model):
    __tablename__ = "media"
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(250), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

class Comment(db.Model):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, ForeignKey('post.id'), nullable=False)

class Follower(db.Model):
    __tablename__ = 'follower'
    user_from_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False, primary_key=True)
    user_to_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False, primary_key=True)

## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e






