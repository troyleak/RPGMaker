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
            # print("Roll: " + str(roll))
            result.append(roll)
            # print("Result: " + str(result))

        return result

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
