from flask import Flask, render_template,request,jsonify

import random

app = Flask(__name__)

@app.route("/")
def board():
    return render_template("tryboard.html")
players = {
    'IronMan-token': {'name': 'IronMan', 'position': 0},
    'HawkEye-token': {'name': 'HawkEye', 'position': 0},
    'Thor-token': {'name': 'Thor', 'position': 0}
}

@app.route('/')
def index():
    return render_template('tryboard.html')

@app.route('/roll_dice', methods=['POST'])
def roll_dice():
    data = request.get_json()
    token = data['token']
    
    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total_roll = die1 + die2
    
    # Move the token
    current_position = players[token]['position']
    new_position = (current_position + total_roll) % 40
    players[token]['position'] = new_position
    
    return jsonify(position=new_position, dice=total_roll, token=token)

if __name__ == '__main__':
    app.run(debug=True,port=9098)

    