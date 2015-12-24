import unittest

from app.character_gen import *
from . import *

class TestCharacter(unittest.TestCase):

  def test_ability_scores(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_race(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_class(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
