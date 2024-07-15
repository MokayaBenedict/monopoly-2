import random
from board import *
from player import *




dice1 = random.randint(1,6)
print(f"player rolled :{dice1}")
dice2 = random.randint(1,6)
print(f"player rolled :{dice2}")

steps_moved = dice1 + dice2 
print(f"steps moved :{steps_moved}")

#def move(player, roll):
#        # Move the player based on the dice roll and update position on the board.
#        player.position = (player.position + roll) % len(board)
#        print(f"{player.token} landed on {board[player.position]['name']}")


def move_player(player: Player, steps: int, board: list, players: list):
    player.position = (player.position + steps) % len(board)
    current_square = board[player.position]
    print(f"{player.name} moved to square {current_square['square']}: {current_square['name']} (${current_square['price']})")


#                                                                                
#def roll_dice() -> tuple:
#    """
#    Rolls two dice and returns the result as a tuple.
#    """
#    dice1 = random.randint(1, 6)
#    dice2 = random.randint(1, 6)
#    print(f"Player rolled: {dice1}, {dice2}")
#    return dice1, dice2
#
#def move_player(player: Player, steps: int, board: list, players: list):
#    """
#    Moves the player on the game board based on the dice roll.
#    Handles rent payments and property ownership.
#    """
#    player.position = (player.position + steps) % len(board)
#    current_square = board[player.position]
#    print(f"{player.name} moved to square {current_square['square']}: {current_square['name']} (${current_square['price']})")
#
#    if current_square['name'] in [prop['name'] for prop in player.properties]:
#        print(f"{player.name} owns this property and doesn't need to pay rent.")
#    elif current_square['price'] == 0 and current_square['name'] in ["Chance", "Community Chest"]:
#        handle_card(player, current_square['name'], players)
#    else:
#        for owner in players:
#            if current_square['name'] in [prop['name'] for prop in owner.properties] and owner != player:
#                rent = current_square['rent'][owner.houses[current_square['name']]]
#                print(f"{player.name} pays ${rent} in rent to {owner.name}")
#                player.money -= rent
#                owner.money += rent
#
#    print(f"Properties owned by {player.name}:")
#    for property in player.properties:
#        print(f"- {property['name']}")
#
#def buy_property(player: Player, square: dict):
#    """
#    Allows a player to buy a property if they have enough money.
#    """
#    if square['price'] <= player.money:
#        player.money -= square['price']
#        player.properties.append(square)
#        print(f"{player.name} bought {square['name']} for ${square['price']}")
#        print(f"{player.name} has cash at hand: ${player.money}")
#    else:
#        print(f"{player.name} does not have enough money to buy {square['name']}")
#
## Example usage
#player = Player("John", 1000)
#board = [{"square": 1, "name": "Go", "price": 0, "rent": [0, 0, 0, 0, 0, 0]},
#         {"square": 2, "name": "Mediterranean Avenue", "price": 60, "rent": [2, 10, 30, 90, 160, 250]}]
#
#dice1, dice2 = roll_dice()
#steps_moved = dice1 + dice2
#move_player(player, steps_moved, board, [player])
#buy_property(player, board[1])
#