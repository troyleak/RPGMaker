import unittest

from app.character_gen.ability_scores import Abilities


class TestAbilityScores(unittest.TestCase):

    def test_init_ability_scores(self):
        result = Abilities()
        self.assertIsInstance(result, Abilities)

    def test_set_ability_stat_rand(self):
        test_object = Abilities()
        test_object.set_ability_stat_rand("strength")
        self.assertIn(test_object.stats["strength"], range(3, 19))

    def test_get_ability_scores(self):
        # Checks that the sum of the returned values
        # are between 54 (8 * 6) and 109 ((18 * 6) + 1)
        # Values being way off indicates errors in randomness
        ability_scores = Abilities()
        result = ability_scores.get_ability_scores()
        self.assertIsInstance(result, dict)
        self.assertIn(sum(result.values()), range(54, 109))

    def test_get_ability_mods(self):
        # Same as above but between -2 and 10, since modifiers
        # should rarely exceed these values
        ability_scores = Abilities()
        result = ability_scores.get_ability_mods()
        self.assertIsInstance(result, dict)
        self.assertIn(sum(result.values()), range((-2), 10))

    def test_set_scores(self):
        ability_scores = Abilities()
        scores = {
            'strength': 18, 'dexterity': 18, 'constitution': 18,
            'intelligence': 18, 'wisdom': 18, 'charisma': 18}
        ability_scores.set_ability_scores(scores)
        self.assertIs(ability_scores.stats['strength'], 18)


if __name__ == '__main__':
    unittest.main()
