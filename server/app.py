#!/usr/bin/env python3

from flask import Flask, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Hero, Power, HeroPower
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.environ.get(
    "DB_URI", f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Code challenge</h1>'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    response_data = [hero.to_dict() for hero in heroes]
    response = make_response(response_data, 200)
    return response


@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        response = make_response(hero.to_dict(), 200)
    else:
        response = make_response({"error": "Hero not found"}, 404)
    return response

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    response_data = [power.to_dict() for power in powers]
    response = make_response(response_data, 200)
    return response

if __name__ == '__main__':
    app.run(port=5555, debug=True)
