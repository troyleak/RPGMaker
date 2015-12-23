
'''
Default constructor creates empty values.
Call set_attribs_rand method on Character object to populate with random
values
Call set_attrib to change an individual parameter
'''

class Character(): # TODO: Add feats

    def __init__(self):

        self.ability_scores = None
        self.attributes = None
        self.skills = None
        self.feats = None
        self.spells = None
        self.char_class = None
        self.gear = None
        self.race = None

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

        self.money = 0
        self.experience = 0

    def create_char(self, ability_scores, attributes, char_class, feats, gear, race, skills, spells):
        self.ability_scores = ability_scores
        self.attributes = attributes
        self.skills = skills
        self.feats = feats
        self.spells = spells
        self.char_class = char_class
        self.gear = gear
        self.race = race


    def set_attrib(self, attrib, value):
    # takes an attribute and a value and sets the value to the passed val
    # checks its own member variables and if that exists, the list of
    # options for that attribute before modifying the value
    # TODO: Move to try/except

        try:
            if attrib in self.__dict__ and value in self.options[attrib]:
                self.__dict__[attrib] = value
        except ValueError:
            print("ERROR - " + attrib + " is not a valid attribute or " + value + " is not a valid option")
        print("test")


    def set_attribs_rand(self):
        # sets attributes randomly
        self.gender = random.choice(gender_opts)
        self.race = random.choice(race_opts)
        self.size = random.choice(size_opts)
        self.age = random.choice(age_opts)
        self.height = random.choice(height_opts)
        self.weight = random.choice(weight_opts)
        self.hair = random.choice(hair_opts)
        self.eyes = random.choice(eyes_opts)
        self.alignment = random.choice(alignment_opts)
