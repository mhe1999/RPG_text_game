import random

class spell:
    def __init__(self , name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        return random.randrange(self.dmg - 15, self.dmg + 15)

    def get_name(self):
        return  self.name

    def get_cost(self):
        return  self.cost
