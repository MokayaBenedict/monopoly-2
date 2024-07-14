from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from player import Player
from computer_logic import computerTurn
from board import board
from cards import draw_card, handle_card, chance_cards, community_chest_cards
from models import db, PlayerModel, PropertyModel, GameModel
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monopoly.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    game = GameModel()
    player1 = PlayerModel(name="Player 1", token="Thor")
    player2 = PlayerModel(name="Computer", token=random.choice(["Strange", "IronMan", "Hawkeye"]), is_computer=True)
    game.players = [player1, player2]
    db.session.add(game)
    db.session.commit()
    session['game_id'] = game.id
    session['current_player_index'] = 0
    return redirect(url_for('play_game'))

@app.route('/play_game', methods=['GET', 'POST'])
def play_game():
    game_id = session.get('game_id')
    game = GameModel.query.get(game_id)
    players = game.players
    current_player_index = session.get('current_player_index', 0)
    current_player = players[current_player_index]

    if request.method == 'POST':
        if 'roll_dice' in request.form:
            dice1, dice2 = current_player.rollDice()
            movePlayer(current_player, dice1 + dice2, players)
            session['current_player_index'] = (current_player_index + 1) % len(players)
            if check_for_bankruptcy(players):
                return redirect(url_for('game_over', winner=players[0].name))
            return redirect(url_for('play_game'))

    return render_template('game.html', current_player=current_player, players=players, board=board)

@app.route('/game_over')
def game_over():
    winner = request.args.get('winner', 'No one')
    return render_template('game_over.html', winner=winner)

def movePlayer(player, roll, players):
    player.move(roll, players)

def check_for_bankruptcy(players):
    for player in players:
        if player.checkBankruptcy():
            players.remove(player)
    if len(players) == 1:
        return True
    return False

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
