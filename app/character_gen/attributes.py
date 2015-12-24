import random

'''
Contains data structures pertaining to character's physical attributes.

Also contains modifiers for base stats. This class will be used last after
race, class, skills, feats, etc. have been selected

self.options: contains a dict with the available options for each physical attribute

set_attrib takes an attribute and a value and modifies the character
    appropriately, if the desired attribute and option exist.
'''

class Attributes():
    def __init__(self):
        self.options = {
            'gender' : ['male', 'female'],
            'size' : ['large', 'medium', 'small'],
            'age' : list(xrange(18, 400)),
            'height' : list(xrange(100, 200)),
            'weight' : list(xrange(150, 300)),
            'hair' : ['red', 'orange', 'yellow', 'green', 'blue',
                      'indigo', 'violet', 'black', 'white'],
            'eyes' : ['red', 'orange', 'yellow', 'green', 'blue',
                      'indigo', 'violet', 'black', 'white'],
            'alignment' : [ 'chaotic_evil', 'chaotic_neutral', 'chaotic_good',
                            'neutral_evil', 'neutral_neutral', 'neutral_good',
                            'lawful_evil', 'lawful_neutral', 'lawful_good' ]
            }

        self.gender = 'none'
        self.size = 'none'
        self.age = 0
        self.height = 0
        self.weight = 0
        self.hair = 'none'
        self.eyes = 'none'
        self.alignment = 'none'

        # misc modifiers
        self.base_attack_bonus = 0
        self.spell_resist = 0
        self.armor_class = 10
        self.ac_touch = 0
        self.ac_flat = 0
        self.speed = 0
        self.initiative = 0
        self.hit_points = 0
        self.armor_bonus = 0
        self.shield_bonus = 0
        self.dodge_bonus = 0
        self.size_mod = 0
        self.natural_armor = 0
        self.deflection_mod = 0
        self.misc_armor_mod = 0
        self.combat_maneuver_bonus = 0
        self.combat_maneuver_defense = 10
        self.class_skills = None
        self.num_feats = 0
        self.languages = None
        self.is_caster = False
        self.spell_failure = 0
        self.character_level = 1
        self.favored_hp = True
        self.build = 'Random'



    def set_attrib(self, attrib, value):
    # takes an attribute and a value and sets the attrib to the passed val
        try:
            self.attrib = value
        except ValueError:
            print("Error modifying that attribute. Perhaps it doesn't exist?")
    # checks its own member variables and if that exists, the list of
    # options for that attribute before modifying the value
        # if attrib in self.__dict__ and value in self.options[attrib]:
        #     self.__dict__[attrib] = value
        # else:
        #     print("Error modifying that attribute. Perhaps it doesn't exist?")
        # print("test")


    def set_attribs_rand(self):
        # sets attributes randomly
        self.gender = random.choice(self.options[gender])
        self.race = random.choice(self.options[race])
        self.size = random.choice(self.options[size])
        self.age = random.choice(self.options[age])
        self.height = random.choice(self.options[height])
        self.weight = random.choice(self.options[weight])
        self.hair = random.choice(self.options[hair])
        self.eyes = random.choice(self.options[eyes])
        self.alignment = random.choice(self.options[alignment])
