import unittest
import json

from app.character_gen.character import *


class TestCharacter(unittest.TestCase):

    def test_init_character(self):
        # Is the character object being created correctly?
        player = Character()
        self.assertIsInstance(player, Character)

    def test_char_to_json(self):
        return self

    def test_assign_stats_from_submitted_list(self):
        test_list_from_form = [
            ('attributes-level', '5'),
            ('skills-sleight_of_hand', ''),
            ('attributes-name', 'Gork'),
            ('attributes-player', 'Troy'),
            ('skills-use_magic_device', ''),
            ('item-item', ''),
            ('skills-knowledge_nature', ''),
            ('abilities-strength', '18'),
            ('skills-knowledge_local', ''),
            ('attributes-homeland', ''),
            ('skills-diplomacy', ''),
            ('skills-disable_device', ''),
            ('skills-spellcraft', ''),
            ('skills-linguistics', ''),
            ('skills-intimidate', ''),
            ('attributes-deity', ''),
            ('submit', 'Submit'),
            ('skills-knowledge_geography', ''),
            ('skills-knowledge_engineering', ''),
            ('skills-sense_motive', ''),
            ('weapon-ammunition', ''),
            ('weapon-name', 'Sword'),
            ('armor-spell_failure', ''),
            ('skills-appraise', ''),
            ('skills-disguise', ''),
            ('skills-knowledge_history', ''),
            ('skills-perform_b', ''),
            ('armor-properties', ''),
            ('abilities-constitution', ''),
            ('armor-check_penalty', ''),
            ('skills-craft_a', ''),
            ('skills-ride', ''),
            ('skills-profession_b', ''),
            ('skills-knowledge_religion', ''),
            ('armor-armor_type', ''),
            ('skills-profession_a', ''),
            ('weapon-damage', ''),
            ('attributes-gender', ''),
            ('item-weight', ''),
            ('weapon-wpn_range', ''),
            ('attributes-hair', ''),
            ('skills-knowledge_planes', ''),
            ('skills-climb', ''),
            ('skills-acrobatics', ''),
            ('attributes-alignment', ''),
            ('skills-fly', ''),
            ('skills-stealth', ''),
            ('skills-knowledge_dungeoneering', ''),
            ('armor-weight', ''),
            ('attributes-height', ''),
            ('skills-perform_a', ''),
            ('attributes-size', ''),
            ('skills-perception', ''),
            ('skills-swim', ''),
            ('skills-craft_b', ''),
            ('attributes-age', ''),
            ('skills-bluff', ''),
            ('attributes-weight', ''),
            ('skills-survival', ''),
            ('abilities-charisma', ''),
            ('weapon-dmg_type', ''),
            ('skills-escape_artist', ''),
            ('skills-knowledge_arcana', ''),
            ('skills-heal', ''),
            ('attributes-race', ''),
            ('armor-name', ''),
            ('abilities-dexterity', ''),
            ('skills-craft_c', ''),
            ('attributes-eyes', ''),
            ('armor-bonus', ''),
            ('skills-knowledge_nobility', ''),
            ('skills-handle_animal', ''),
            ('abilities-wisdom', ''),
            ('weapon-critical', ''),
            ('weapon-attack_bonus', ''),
            ('abilities-intelligence', '')]

        player = Character()
        player.assign_stats_from_submitted_list(test_list_from_form)

        return self


if __name__ == '__main__':
    unittest.main()
