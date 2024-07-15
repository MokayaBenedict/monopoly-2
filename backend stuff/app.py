

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
from config import Config  
from dotenv import load_dotenv
import psycopg2

db = SQLAlchemy()
load_dotenv()
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    return app
app = create_app()


class DiceRoll(db.Model):
    __tablename__ = 'dice_roll'
    id = db.Column(db.Integer, primary_key=True)
    roll1 = db.Column(db.Integer, nullable=False)
    roll2 = db.Column(db.Integer, nullable=False)

@app.route('/roll_dice', methods=['GET'])
def roll_dice():
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

    dice_roll = DiceRoll(roll1=roll1, roll2=roll2)
    db.session.add(dice_roll)
    db.session.commit()

    return jsonify(dice_roll.serialize())

@app.route('/hey', methods=['GET'])
def helloworld():
 return "Hello World!"
 

if __name__ == '__main__':
    app.run(debug=True,port=9095)