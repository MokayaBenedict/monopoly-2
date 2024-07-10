from main import *
from property import*
from player import*
def computer_decision(buy_property,player: Player, board: list):
    """Make decisions for the computer player."""
    if player.money > 500:
        # Buy properties
        for square in board:
            if square['price'] > 0 and square['name'] not in [prop['name'] for prop in player.properties] and player.money >= square['price']:
             buy_property(player, square)
            break


    elif player.money < 200:
        # Mortgage properties
        for property in player.properties:
            if property not in player.mortgaged_properties:
                player.mortgage(property['name'])
                break