'''
Class Class (classy)

Contains class logic. I expect this one to be quite fun

For now skills and stats will be modified. Feats may come later

'''


class Char_Class():
    def __init__(self):
        self.choices = [
            'barbarian', 'bard', 'cleric', 'druid',
            'fighter', 'monk', 'paladin', 'ranger',
            'rogue', 'sorcerer', 'wizard'
        ]
        self.class_skill_list = []
        self.hit_die = []
        self.skill_ranks_per_lvl = []
        self.level_stats = {
            'base_attack_bonus': '',
            'fortitude': '', 'reflex': '', 'will': ''}

    def make(self, master, char_class):
        if char_class in self.choices:
            if char_class == 'barbarian':
                master.char_class = Barbarian()
                print("barbarian")

            if char_class == 'bard':
                master.char_class = Bard()
                print("bard")

            if char_class == 'cleric':
                master.char_class = Cleric()
                print("cleric")

            if char_class == 'druid':
                master.char_class = Druid()
                print("druid")

            if char_class == 'fighter':
                master.char_class = Fighter()
                print("fighter")

            if char_class == 'monk':
                master.char_class = Monk()
                print("monk")

            if char_class == 'paladin':
                master.char_class = Paladin()
                print("paladin")

            if char_class == 'ranger':
                master.char_class = Ranger()
                print("ranger")

            if char_class == 'rogue':
                master.char_class = Rogue()
                print("rogue")

            if char_class == 'sorcerer':
                master.char_class = Sorcerer()
                print("sorcerer")

            if char_class == 'wizard':
                master.char_class = Wizard()
                print("wizard")

    def calc_bab(self, level):
        # Takes a level, returns a list of Base Attack Bonuses for it
        value = []

        while (level > 0):
            value.append(level)
            level -= 5  # Breaks loop before appending if level < 5
        value.sort()
        return value

    def calc_save(save, level, my_mod, my_bonus):
        # my_mod must be a three-tuple of floats in fort ref will order
        # my bonus must be a three-tuple in the same order, representing the
        # bonus of the class. EG: Barbarian has a +2 in fort
        # my_mod would be (2.0, 3.0, 4.0)
        # my_bonus would be (2, 0, 0)
        valid_saves = ['fort', 'ref', 'will']
        if save not in valid_saves:
            print("ERROR: not a valid saving throw value")
            return 0
        else:
            result = {}
            for i in range(1, 4):
                tmp = {
                    valid_saves[i]: int((1 / my_mod[i]) + my_bonus[i])}
                result.append(tmp)
            return result

    def get_spells_mod(self, my_mod):
        def calc_mod(my_mod):
            print("not implemented yet")  # TODO: implement this
        return calc_mod


class Barbarian(Char_Class):
    def __init__(self):

        self.class_skill_list = [
            "Acrobatics", "Climb", "Craft",
            "Handle Animal", "Intimidate", "Knowledge: Nature",
            "Perception", "Ride", "Survival", "Swim"]

        self.hit_die = {
            'number': 2,
            'sides': 10
            }
        self.save_mods = {
            'fort': 2.0,
            'ref': 3.0,
            'will': 4.0
            }
        self.save_bonus = {
            'fort': 2,
            'ref': 0,
            'will': 0
            }
        self.save_throws_final = Char_Class.calc_save(self.save_mods, self.save_bonus)

    # Fast movement, rage
    # Rage power, uncanny dodge
    # Trap sense +1
    # Rage power
    # Improved uncanny dodge
    # Rage power, Trap sense +2
    # Damage reduction 1/—
    # Rage power
    # Trap sense +3
    # Damage reduction 2/—, Rage power Greater rage
    # Rage power, Trap sense +4
    # Damage reduction 3/—
    # Indomitable will, Rage power
    # Trap sense +5
    # Damage reduction 4/—, Rage power Tireless rage
    # Rage power, Trap sense +6
    # Damage reduction 5/—
    # Mighty rage, Rage power

    def calc_bab(level):
        # Takes a level, returns a list of Base Attack Bonuses for that level
        value = [level]

        while (level > 0):
            value.append(level)
            level -= 5  # Breaks loop before appending if level < 5
        return level

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Bard(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Acrobatics", "Appraise", "Bluff", "Climb", "Diplomacy",
            "Disguise", "Escape Artist", "Intimidate", "Knowledge: Arcana",
            "Knowledge: Dungeoneering", "Knowledge: Engineering",
            "Knowledge: Geography", "Knowledge: History", "Knowledge: Local",
            "Knowledge: Nature", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Perception", "Perform",
            "Profession", "Sense Motive", "Sleight of Hand", "Spellcraft",
            "Stealth", "Use Magic Device"]

    def make(self, character):
        character.class_skills = self.class_skill_list
        print("test")


class Cleric(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Appraise", "Craft", "Diplomacy", "Heal", "Knowledge: Arcana",
            "Knowledge: History", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Profession", "Sense Motive",
            "Spellcraft"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Druid(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Climb", "Craft", "Fly", "Handle Animal", "Heal",
            "Knowledge: Geography", "Knowledge: Nature",
            "Perception", "Profession", "Ride", "Spellcraft",
            "Survival", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Fighter(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Climb", "Craft", "Handle Animal", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Engineering", "Profession",
            "Ride", "Survival", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Monk(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Acrobatics", "Climb", "Craft", "Escape Artist", "Intimidate",
            "Knowledge: History", "Knowledge: Religion", "Perception",
            "Perform", "Profession", "Ride", "Sense Motive",
            "Stealth", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Paladin(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Craft", "Diplomacy", "Handle Animal", "Heal",
            "Knowledge: Nobility", "Knowledge: Religion",
            "Profession", "Ride", "Sense Motive", "Spellcraft"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Ranger(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Climb", "Craft", "Handle Animal", "Heal", "Heal", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Geography",
            "Knowledge: Nature", "Perception", "Profession", "Ride",
            "Spellcraft", "Stealth", "Survival", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Rogue(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Acrobatics", "Appraise", "Bluff", "Climb", "Craft", "Diplomacy",
            "Disable Device", "Disguise", "Escape Artist", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Local",
            "Linguistics", "Perception", "Perform",
            "Profession", "Sense Motive", "Sleight of Hand", "Stealth",
            "Swim", "Use Magic Device"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Sorcerer(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Appraise", "Bluff", "Craft", "Fly", "Intimidate",
            "Knowledge: Arcana", "Profession", "Spellcraft",
            "Use Magic Device"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Wizard(Char_Class):
    def __init__(self):
        self.class_skill_list = [
            "Appraise", "Craft", "Fly", "Knowledge: Arcana",
            "Knowledge: Dungeoneering", "Knowledge: Engineering",
            "Knowledge: Geography", "Knowledge: History", "Knowledge: Local",
            "Knowledge: Nature", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Profession", "Spellcraft"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")
