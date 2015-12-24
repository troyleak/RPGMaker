import unittest

from app.character_gen.ability_scores import Abilities

class TestAbilityScores(unittest.TestCase):

    def test_set_ability_stat_rand(self):
        stat = "strength"
        result = Abilities.set_ability_stat_rand(self, stat)
        self.assertIsInstance(result, int)
        self.assertIn(result, range(3, 19))


    def test_get_ability_scores(self):
        # Checks that the sum of the returned values
        # are between 54 (8 * 6) and 109 ((18 * 6) + 1)
        # Values being way off indicates errors in randomness
        ability_scores = Abilities()
        result = ability_scores.get_ability_scores()
        self.assertIsInstance(result, list)
        self.assertIn(sum(result), range(54, 109))


    def test_get_ability_mods(self):
        # Same as above but between -2 and 10, since modifiers
        # should rarely exceed these values
        ability_scores = Abilities()
        result = ability_scores.get_ability_mods()
        self.assertIsInstance(result, list)
        self.assertIn(sum(result), range((-2), 10))

if __name__ == '__main__':
    unittest.main()
