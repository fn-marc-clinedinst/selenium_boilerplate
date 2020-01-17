from random import randint


class Dice:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

    def roll(self):
        return randint(1, self.number_of_sides)
