import unittest

from app.character_gen import character, classes


class TestCharClass(unittest.TestCase):

    def test_make_classes(self):
        obj = character.Character()
        obj.char_class.make(obj, 'barbarian')
        self.assertIsInstance(obj.char_class, classes.Barbarian)

    def test_base_attack_bonus(self):
        obj = character.Character()
        for i in range(1, 6):
            # tests that the first 5 levels return BAB equal to their value
            self.assertEqual(obj.char_class.calc_bab(i), [i])
        for i in range(6, 11):
            self.assertEqual(obj.char_class.calc_bab(i), [(i-5), i])

        for i in range(11, 16):
            self.assertEqual(obj.char_class.calc_bab(i), [(i-10), (i-5), i])

        for i in range(16, 21):
            self.assertEqual(obj.char_class.calc_bab(i), [(i-15), (i-10),
                                                          (i-5), i])

    # def test_saving_throws(self):
    #     obj = character.Character()
    #     obj.char_class.get_save_mod(obj.char_class., 'barbarian')
    #
    #     self.assertEqual(obj.char_class.hit_die, [2, 10])


if __name__ == '__main__':
    unittest.main()
