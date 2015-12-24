
'''
Default constructor creates empty values.
Call set_attribs_rand method on Character object to populate with random
values
Call set_attrib to change an individual parameter
'''

class Character(): # TODO: Add feats

    def __init__(self):

        self.ability_scores = None
        self.race = None
        self.char_class = None
        self.skills = None
        self.feats = None
        self.spells = None
        self.gear = None
        self.attributes = None

        self.money = 0
        self.experience = 0

    def create_char(self, ability_scores, attributes, char_class, feats, gear, race, skills, spells):
        self.ability_scores = ability_scores
        self.race = race
        self.char_class = char_class
        self.skills = skills
        self.feats = feats
        self.spells = spells
        self.gear = gear
        self.attributes = attributes
