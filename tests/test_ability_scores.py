import unittest

from app.character_gen.ability_scores import Abilities

class TestAbilityScores(unittest.TestCase):

    def test_set_ability_scores_rand(self):
        stat = "Strength"
        result = Abilities.set_ability_stat_rand(self, stat)
        self.assertIsInstance(result, int)
        self.assertIn(result, range(3, 19))



if __name__ == '__main__':
    unittest.main()
