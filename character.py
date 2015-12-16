# RPG Character Generator
# Create a database filled with different character classes, stats that fall
# within each class’ restrictions (wizards could always have low strength but
# high magic for example), and maybe even a description generator populated
# with premade sentences pertaining to personality, skill, and history. For an
# interface, allow the user to select what kind of class or character they’d
# like, and a ROLL or GENERATE button that will fill in the rest.
#
# Bonus points: provide a print button that will produce a
# printer-friendly version of the character sheet.

'''
Default constructor creates random/empty values.
Call create method on Character object to populate with values
'''

import random
from collections import namedtuple

from skills import *

class Character(Skills): # TODO: Add feats

    def __init__(self, master):

        # abilities
        Ability = namedtuple('Ability', ['stat', 'mod'])

        self.strength = Ability(0, 0)
        self.dexterity = Ability(0, 0)
        self.constitution = Ability(0, 0)
        self.intelligence = Ability(0, 0)
        self.wisdom = Ability(0, 0)
        self.charisma = Ability(0, 0)

        # attributes
        self.gender = 'none'
        self.race = 'none'
        self.size = 'none'
        self.age = 0
        self.height = 0
        self.weight = 0
        self.hair = 'none'
        self.eyes = 'none'
        self.alignment = 'none'

        # Saving throws and modifiers
        self.fortitude = 0
        self.fort_magic_mod = 0
        self.fort_misc_mod = 0
        self.reflex = 0
        self.reflex_magic_mod = 0
        self.reflex_misc_mod = 0
        self.will = 0
        self.will_magic_mod = 0
        self.will_misc_mod = 0

        self.base_attack_bonus = 0
        self.spell_resist = 0
        self.armor_class = 10
        self.ac_touch = 0
        self.ac_flat = 0
        self.speed = 0
        self.initiative = 0
        self.hp = 0
        self.armor_bonus = 0
        self.shield_bonus = 0
        self.dodge_bonus = 0
        self.size_mod = 0
        self.natural_armor = 0
        self.deflection_mod = 0
        self.misc_armor_mod = 0
        self.cmb = 0
        self.cmd = 10
        self.class_skills = None
        self.skills = None
        self.num_feats = 0
        self.feats = None
        self.spells = None
        self.languages = None
        self.is_caster = False
        self.spell_failure = 0
        self.char_class = None
        self.character_level = 1
        self.favored_hp = True
        self.build = 'Random'

        self.items = []
        self.money = 0
        self.experience = 0


    def roll_die(self, sides):
        try:
            random.seed(random.seed(random.random))
            return random.randrange(1, sides+1)
        except ValueError:
            print("Error, invalid number of sides")


    def set_ability_stat(self):
        lst = []
        for i in range(4):
            tmp = self.roll_die(self, 6)
            lst.append(tmp)
        lst.sort(reverse=True)
        lst.pop()
        result = 0
        for i in lst:
            result += i
        return result


    def set_ability_mod(self, stat):
        if stat >= 10:
            modifier = (stat - 10) / 2
        elif stat < 10:
            modifier = (11 - stat) / 2 * -1
        return modifier

    def create():
        print("Hello World")
