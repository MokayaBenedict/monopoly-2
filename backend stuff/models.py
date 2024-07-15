from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PlayerModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    token = db.Column(db.String(50), nullable=False)
    is_computer = db.Column(db.Boolean, default=False)
    money = db.Column(db.Integer, default=1500)
    position = db.Column(db.Integer, default=0)
    in_jail = db.Column(db.Boolean, default=False)
    jail_turns = db.Column(db.Integer, default=0)
    get_out_of_jail_free = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Player {self.name}>'

class PropertyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    rent = db.Column(db.PickleType, nullable=False)  # Stores list of rent values
    owner_id = db.Column(db.Integer, db.ForeignKey('player_model.id'), nullable=True)
    mortgaged = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Property {self.name}>'

class GameModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    players = db.relationship('PlayerModel', backref='game', lazy=True)
    current_player_index = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Game {self.id}>'
