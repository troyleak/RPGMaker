import random

class Dice():

    def roll_dice(sides, dice):
        # returns a list of the outcome of the specified number of die rolls
        random.seed(random.seed(random.random))

        if dice == 0:
            dice = 1
        # If no dice are input, default to 1

        result = []

        for i in range(dice):
            result.append(random.randrange(1, sides+1))

        return result
