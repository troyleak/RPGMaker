import unittest

from app.character_gen.dice import Dice



class TestDice(unittest.TestCase):

  def test_dice_spread(self):
      # test that the dice function returns statistically valid results
      sides = [2, 3, 4, 6, 8, 10, 12, 20, 100]
      for rolls in range(1, 20):
          for j in sides:
              roll = sum(Dice.roll_dice(j, rolls))
              lo = (rolls) # boundary if we rolled all 1s
              hi = ((rolls * j) + 1)
              self.assertIn(roll, range(lo, hi))


if __name__ == '__main__':
    unittest.main()
