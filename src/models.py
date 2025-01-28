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
    id = db.Column(db.Integer, primary_key=True, unique = True)
    username = db.Column(db.String(250), nullable=False, unique = True)
    password = db.Column(db.String(250), nullable=False)
    favourite_list = db.Column(db.String(250), ForeignKey('favourite_list.id'), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique = True)

class Favourite_list(db.Model):
    __tablename__ = 'favourite_list'
    id = db.Column(db.Integer, primary_key=True)
    user_favourite_id = db.Column(db.String(250), ForeignKey('user.id'), nullable=False)




class Starships(db.Model):
    __tablename__ = "starships"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250), nullable=False, unique = True)
    starship_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.String(250))
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    hyperdrive_rating = db.Column(db.String(250))
    MGLT = db.Column(db.String(250))
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(250))
    pilots = db.Column(db.String(250))

class Vehicles(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(250), nullable=False, unique = True)
    vehicle_class = db.Column(db.String(250))
    manufacturer = db.Column(db.String(250))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.String(250))
    passengers = db.Column(db.Integer)
    max_atmosphering_speed = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    consumables = db.Column(db.String(250))
    pilots = db.Column(db.String(250))

class Species(db.Model):
    __tablename__ = "species"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False, unique = True)
    classification = db.Column(db.String(250))
    designation = db.Column(db.String(250))
    average_height = db.Column(db.Integer)
    average_lifespan = db.Column(db.Integer)
    hair_colors = db.Column(db.String(250))
    skin_colors = db.Column(db.String(250))
    eye_colors = db.Column(db.String(250))
    homeworld = db.Column(db.String(250))
    language = db.Column(db.String(250))


## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e






