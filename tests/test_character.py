import unittest
import json

from app.character_gen.character import *


class TestCharacter(unittest.TestCase):

    def test_init_character(self):
        # Is the character object being created correctly?
        player = Character()
        self.assertIsInstance(player, Character)

    def test_char_to_json(self):
        player = Character()
        self.assertIsInstance(player, Character)
        player = player.to_json()
        self.assertIsInstance(player, str)

    def test_assign_stats_from_submitted_list(self):
        test_list_from_form = [
            ('abilities-charisma', '18'),
            ('abilities-constitution', '18'),
            ('abilities-dexterity', '18'),
            ('abilities-intelligence', '18'),
            ('abilities-strength', '18'),
            ('abilities-wisdom', '18'),
            ('armor-armor_type', ''),
            ('armor-bonus', ''),
            ('armor-check_penalty', ''),
            ('armor-name', ''),
            ('armor-properties', ''),
            ('armor-spell_failure', ''),
            ('armor-weight', ''),
            ('attributes-age', '30'),
            ('attributes-alignment', ''),
            ('attributes-deity', ''),
            ('attributes-eyes', 'blue'),
            ('attributes-gender', 'male'),
            ('attributes-hair', 'brown'),
            ('attributes-height', '150'),
            ('attributes-homeland', ''),
            ('attributes-level', '5'),
            ('attributes-name', 'Gork'),
            ('attributes-player', 'Troy'),
            ('attributes-race', ''),
            ('attributes-size', ''),
            ('attributes-weight', ''),
            ('item-item', 'coin'),
            ('item-weight', '1'),
            ('skills-acrobatics', ''),
            ('skills-appraise', ''),
            ('skills-bluff', ''),
            ('skills-climb', ''),
            ('skills-craft_a', ''),
            ('skills-craft_b', ''),
            ('skills-craft_c', ''),
            ('skills-diplomacy', ''),
            ('skills-disable_device', ''),
            ('skills-disguise', ''),
            ('skills-escape_artist', ''),
            ('skills-fly', ''),
            ('skills-handle_animal', ''),
            ('skills-heal', ''),
            ('skills-intimidate', ''),
            ('skills-knowledge_arcana', ''),
            ('skills-knowledge_dungeoneering', ''),
            ('skills-knowledge_engineering', ''),
            ('skills-knowledge_geography', ''),
            ('skills-knowledge_history', ''),
            ('skills-knowledge_local', ''),
            ('skills-knowledge_nature', ''),
            ('skills-knowledge_nobility', ''),
            ('skills-knowledge_planes', ''),
            ('skills-knowledge_religion', ''),
            ('skills-linguistics', ''),
            ('skills-perception', ''),
            ('skills-perform_a', ''),
            ('skills-perform_b', ''),
            ('skills-profession_a', ''),
            ('skills-profession_b', ''),
            ('skills-ride', ''),
            ('skills-sense_motive', ''),
            ('skills-sleight_of_hand', ''),
            ('skills-spellcraft', ''),
            ('skills-stealth', ''),
            ('skills-survival', ''),
            ('skills-swim', ''),
            ('skills-use_magic_device', ''),
            ('submit', 'Submit'),
            ('weapon-ammunition', ''),
            ('weapon-attack_bonus', ''),
            ('weapon-critical', ''),
            ('weapon-damage', ''),
            ('weapon-dmg_type', ''),
            ('weapon-name', 'Sword'),
            ('weapon-wpn_range', '')]

        player = Character()
        player.assign_stats_from_submitted_list(test_list_from_form)
        self.assertIsInstance(player, Character)
        self.assertIn("Sword", player.gear.weapons)


if __name__ == '__main__':
    unittest.main()
