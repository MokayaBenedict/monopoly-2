from player import*
class Property:
    def __init__(self, name, price, rent, color_group, house_cost, hotel_cost):
        self.name = name
        self.price = price
        self.rent = rent
        self.color_group = color_group
        self.num_houses = 0
        self.num_hotels = 0
        self.owner = None
        self.is_mortgaged = False
        self.house_cost = house_cost
        self.hotel_cost = hotel_cost

#check if property is already owned
#if property has no owner it is bought

    def buy_property(self, owner):
        if self.owner is None:
            self.owner = owner
        else:
            raise Exception("Property already owned")

#checks if property is mortgaged and  sets it to true if not
#allows the user to mortgage property
    def mortgage_property(self):
        if not self.is_mortgaged:
            self.is_mortgaged = True
        else:
            raise Exception("Property is already mortgaged")
#checks if property is mortgaged and sets it to false if so
#allows the user to unmortgage the property

    def unmortgage_property(self):
        if self.is_mortgaged:
            self.is_mortgaged = False
        else:
            raise Exception("Property is not mortgaged")


#allows the owner to build a house on the property
    def build_house(self):
        if self.num_hotels == 0: #if the property has no hotel it adds the number of houses by 1 
            self.num_houses += 1
        else:
            raise Exception("Cannot build houses after building a hotel")#if the property already has an hotel, you cant build houses to it


#allows the owner to build a hotel on the property
#check if the property has 4 houses so to allow for hotel construction

    def build_hotel(self):
        if self.num_houses == 4:
            self.num_houses = 0
            self.num_hotels += 1
        else:
            raise Exception("Need 4 houses to build a hotel")

#calculates rent for the property based on the number of houses and hotels
#rent cannot be collected on mortgaged property
    def calculate_rent(self):
        if self.is_mortgaged:
            return 0
        base_rent = self.rent[0]
        if self.num_hotels > 0:
            return self.rent[5]
        return base_rent + self.num_houses * self.rent[self.num_houses]


# Example usage:
# Creating a property
boardwalk = Property(
    name="Boardwalk",
    price=400, rent=[50, 200, 600, 1400, 1700, 2000],
    color_group="Dark Blue", 
    house_cost=200, 
    hotel_cost=200
    )

# Buying the property
boardwalk.buy_property("player")

# Building houses
boardwalk.build_house()
boardwalk.build_house()

# Calculating rent
print(boardwalk.calculate_rent())  # Output will vary based on the number of houses/hotels

# Mortgaging the property
boardwalk.mortgage_property()

# Unmortgaging the property
boardwalk.unmortgage_property()