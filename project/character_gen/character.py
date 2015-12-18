
'''
Default constructor creates empty values.
Call set_attribs_rand method on Character object to populate with random values
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

        self.money = 0
        self.experience = 0

    def create_char(character_, ability_scores_, attributes_, char_class_, feats_, gear_, race_, skills_, spells_):
        character_.ability_scores = ability_scores_
        character_.attributes = attributes_
        character_.skills = skills_
        character_.feats = feats_
        character_.spells = spells_
        character_.char_class = char_class_
        character_.gear = gear_
        character_.race = race_


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
