import unittest

from app.character_gen.dice import Dice

class TestDice(unittest.TestCase):

  def test_dice_spread(self):
      # test that the dice function returns statistically valid results
      sides = [2, 3, 4, 6, 8, 10, 12, 20, 100]
      for i in xrange(1, 11):
          self.assertIn(number, b)


if __name__ == '__main__':
    unittest.main()
