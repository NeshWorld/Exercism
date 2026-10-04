import random
import math

class Character:
    def __init__(self):
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        lst = []
        for _ in range(4):
            lst.append(random.randint(1, 6))
        lst.remove(min(lst))
        lst = sum(lst)
        return lst


def modifier(value):
    result = math.floor((value - 10)/ 2)
    return result
