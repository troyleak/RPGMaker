import random


class Dice():

    def __init__(self):
        pass

    def roll_dice(sides, dice):
        # returns a list of the outcome of the specified number of die rolls
        random.seed(random.seed(random.random))
        result = []

        for i in range(dice):
            roll = random.randint(1, sides)
            result.append(roll)

        return result

    def drop_lowest(values):
        if len(values) <= 1:
            pass
        else:
            values.sort(reverse=True)
        return values
