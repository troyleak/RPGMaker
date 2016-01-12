import unittest
import random

from app.character_gen.dice import Dice


class TestDice(unittest.TestCase):

    def test_dice_spread(self):
        # test that the dice function returns statistically valid results
        valid_sides = [2, 3, 4, 6, 8, 10, 12, 20, 100]
        for rolls in range(1, 20):
            for sides in valid_sides:
                roll = sum(Dice.roll_dice(sides, rolls))
                lo = (rolls)  # boundary if we rolled all 1s
                hi = ((rolls * sides) + 1)  # ceiling for upper range
                self.assertIn(roll, range(lo, hi))

    def test_dice_drop_lowest(self):
        random.seed()

        test_list = []

        for i in range(5):
            test_list.append(random.randint(0, 100))
            # build a list of 5 random numbers between 0 and 100 to test

        Dice.drop_lowest(test_list)


if __name__ == '__main__':
    unittest.main()
