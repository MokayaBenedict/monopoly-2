import random
#import random module for dice rolling.
from board import *
from comp import *



class Player:
    def __init__ (self, name, token=None, properties=None):
        #t initialize both token and properties to none for player to select later on.
        self.name = name
        #self.token = token
        self.token = token if token is not None else self.tokenSelection()
        self.money = 1500
        #self.properties = properties
        self.properties = properties if properties is not None else [] 
        #if property is not not None, the self.properties is assigned value of properties
        #if property is None, self.properties is assigned an empty list.
        self.mortgaged_properties = []
        # self.jail_turns = 0
        # self.consecutive_doubles = 0
        # self.get_out_of_jail_free = False
        self.position=0

    # def tokenSelection(self):
    #     # an instance method for token selection.
    #     tokens = ["Thor", "strange", "IronMan", "Hawkeye",]
    #     print("Choose your token:")
    def tokenSelection(self):
        tokens = ["Thor", "Strange", "IronMan", "Hawkeye"]
        print("Choose your token:")
        for i, token in enumerate(tokens):
            print(f"{i + 1}. {token}")
        choice = int(input("Enter the number of your choice: ")) - 1
        while choice < 0 or choice > len(tokens):
            print("Invalid choice. Please choose again.")
            choice = int(input("Enter the number of your choice: ")) - 1
        return tokens[choice]
        # return random.choice(tokens) chosed by player.
       

    def rollDice(self):
        # Method to simulate rolling two six-sided dice.
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        moved1 = die1
        moved2 = die2
        movedTo = die1 + die2
        print(f"hey, you rolled {moved1} and {moved2}")
        print(f"You rolled a total of {movedTo}")
        return die1, die2

    # def move(self, roll):
    #     # Move the player based on the dice roll and update position on the board.
    #     self.position = (self.position + roll) % len(board)
    #     print(f"{self.token} landed on {board[self.position]['name']}")
    def move(player, roll):
     player.position = (player.position + roll) % len(board)
     #the modula operation wraps around the board
     current_square = board[player.position]
     print(f"{player.name} moved to square {current_square['square']}: {current_square['name']} (${current_square['price']})")


       
    def buyProperty(self):
        property = board[self.position]
        if property not in self.properties and property not in self.mortgaged_properties:
            if self.money >= property['price']:
                
                self.properties.append(property)
                #add to player's properties list
                
                print(f"{self.token} bought {property['name']} for ${property['price']}")
                self.money = self.money - property['price']
                print(f"Your balance is:{self.money}")
            else:
                print(f"{self.token} does not have enough money to buy {property['name']}")
        else:
            print(f"{property['name']} is already owned.")

        

def mortgaging(self):
        if not self.properties: 
            print(f"{self.token}, you do not own any properties.")
            return

        print(f"{self.token}, you own the following properties:")
        for i, property in enumerate(self.properties, 1):
            print(f"{i}. {property['name']}")

        choice = int(input("Enter the number of the property you want to mortgage (0 to cancel): "))
        
        if choice == 0:
            return

        if 1 <= choice <= len(self.properties):
            property_to_mortgage = self.properties[choice - 1]
            mortgageValue = property_to_mortgage['price'] // 2

            self.money += mortgageValue
            self.mortgaged_properties.append(property_to_mortgage)
            self.properties.remove(property_to_mortgage)
            property_to_mortgage['is_mortgaged'] = True

            print(f"{self.token} mortgaged {property_to_mortgage['name']} for ${mortgageValue}")
        else:
            print("Invalid choice.")


def movePlayer(player, roll):
    player.move(roll)



def play_game():
    global player1, player2
    print("Player 1, please select your token.")
    player1 = Player("Player 1")
    remaining_tokens = ["Thor", "Strange", "IronMan", "Hawkeye"]
    remaining_tokens.remove(player1.token)
    player2 = Player("Computer", token=random.choice(remaining_tokens))


    current_player = player1
    

    while True:
        print(f"\n{current_player.token}'s turn.")
        input("Press Enter to roll the dice.\n")
        dice1, dice2 = current_player.rollDice()
        movePlayer(current_player, dice1 + dice2)

        property = board[current_player.position]
        if property not in current_player.properties and property not in current_player.mortgaged_properties:
            print(f"\n{current_player.token}, do you want to buy {property['name']} for ${property['price']}?")
            buy_option = input("Press 'yes' to buy or 'no' to skip: ").lower()
            if buy_option == 'yes':
                current_player.buyProperty()

        print(f"\n{current_player.token}, do you want to mortgage a property?")
        mortgage_option = input("Press 'yes' to mortgage or 'no' to continue: ").lower()
        if mortgage_option == 'yes':
            mortgaging(current_player)
        
        current_player = player1 if current_player == player2 else player2
        #switch btwn player1 and player2
        if current_player ==player2:
         print("Comps turn")
         while True:
             print(f"\n{current_player.token}'s turn.")
      


            
       
        





        

play_game()