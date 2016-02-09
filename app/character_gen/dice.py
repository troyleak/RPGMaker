import random


class Dice():

    def __init__(self):
        pass

    def roll_dice(sides, dice):
        # generator expression for the given number of dice rolls
        random.seed(random.seed(random.random))
        for i in range(dice):
            yield random.randint(1, sides)

    def drop_lowest(values):
        if len(values) <= 1:
            pass
        else:
            # print("Values1: " + str(values))
            values.sort(reverse=True)
            # print("Values2: " + str(values))
            values.pop()
            # print("Values3: " + str(values))
        return values
