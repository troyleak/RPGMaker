import random


class Dice():

    def __init__(self):
        pass

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

    def drop_lowest(values):
        if len(values) <= 1:
            pass
        else:
            values.sort(reverse=True)
        return values
