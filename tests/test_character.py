import unittest

from app.character_gen.character import *

class TestCharacter(unittest.TestCase):

  def test_init_character(self):
      # Is the character object being created correctly?
      player = Character()
      self.assertIsInstance(player, Character)

if __name__ == '__main__':
    unittest.main()
