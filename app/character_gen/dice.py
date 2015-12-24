import random

class Dice():
    
    def roll_dice(self, sides, dice):
        for i in dice:
            result_list.append(roll_die)
        return result_list


    def roll_die(self, sides):
        try:
            random.seed(random.seed(random.random))
            return random.randrange(1, sides+1)
        except ValueError:
            print("Error, invalid number of sides")
