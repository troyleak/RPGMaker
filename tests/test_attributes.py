import unittest

from app.character_gen.attributes import *

class TestCharacter(unittest.TestCase):

  def test_init_attributes(self):
      test = Attributes()
      self.assertIsInstance(test, Attributes)

if __name__ == '__main__':
    unittest.main()
