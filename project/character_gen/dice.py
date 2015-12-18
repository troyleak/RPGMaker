import random

class Dice():
    def roll_dice(self, sides, dice):
        print("test")


    def roll_die(self, sides):
        try:
            random.seed(random.seed(random.random))
            return random.randrange(1, sides+1)
        except ValueError:
            print("Error, invalid number of sides")
