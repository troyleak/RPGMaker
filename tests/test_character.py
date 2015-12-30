import unittest
import pickle

from app.character_gen.character import *

class TestCharacter(unittest.TestCase):

    def test_init_character(self):
        # Is the character object being created correctly?
        player = Character()
        self.assertIsInstance(player, Character)

    def test_char_to_pickle(self):
        player = Character().char_to_pickle()
        # self.assertIn('strength', player)
        self.assertIsInstance(player, bytes)
        player = pickle.loads(player)
        self.assertIsInstance(player, Character)


if __name__ == '__main__':
    unittest.main()
