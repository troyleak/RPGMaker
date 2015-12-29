
'''
Default constructor creates empty values.
Call set_attribs_rand method on Character object to populate with random
values
Call set_attrib to change an individual parameter
'''

from . import ability_scores, attributes, classes, feats, gear, race, skills, spells

class Character(): # TODO: Add feats

    def __init__(self):

        self.ability_scores = ability_scores.Abilities()
        self.race = race.Race()
        self.char_class = classes.Char_Class()
        self.skills = skills.Skills()
        self.feats = feats.Feats()
        self.spells = spells.Spells()
        self.gear = gear.Gear()
        self.attributes = attributes.Attributes()

        self.money = 0
        self.experience = 0

    def __iter__(self):
        # Overrides iter to output the character class in a sensible way
        result = []

        for _val_ in self.__dict__:
            ## needs to check if _val_ is a member class or if it's a value
            # if it's a value print it, otherwise defer to child obj __iter__
            result.append(vars(self.i.__dict__))

        return result


    # should recreate this to change one class. Can be iterated over a list of classes to change them
    def create_char(self, ability_scores, attributes, char_class, feats, gear, race, skills, spells):
        self.ability_scores = ability_scores
        self.race = race
        self.char_class = char_class
        self.skills = skills
        self.feats = feats
        self.spells = spells
        self.gear = gear
        self.attributes = attributes

    def assign_stats(self, stat, scores):
        return self
