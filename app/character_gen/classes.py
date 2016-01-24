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

    def make(self, char_class):
        if char_class in self.choices:
            if char_class == 'barbarian':
                print("barbarian")

            if char_class == 'bard':
                print("bard")

            if char_class == 'cleric':
                print("cleric")

            if char_class == 'druid':
                print("druid")

            if char_class == 'fighter':
                print("fighter")

            if char_class == 'monk':
                print("monk")

            if char_class == 'paladin':
                print("paladin")

            if char_class == 'ranger':
                print("ranger")

            if char_class == 'rogue':
                print("rogue")

            if char_class == 'sorcerer':
                print("sorcerer")

            if char_class == 'wizard':
                print("wizard")

    def get_bab_mod(mod):
        # Modulates based on number of levels between upgrades
        def calc_bab(level):
            # Takes a level, returns a list of Base Attack Bonuses for it
            value = [level]

            while (level > 0):
                value.append(level)
                level -= mod  # Breaks loop before appending if level < 5
            return level
        return calc_bab

    def get_save_mod(my_mod, my_bonus):
        # my_mod must be a three-tuple of floats in fort ref will order
        # my bonus must be a three-tuple in the same order, representing the
        # bonus of the class. EG: Barbarian has a +2 in fort
        # my_mod would be (2.0, 3.0, 4.0)
        # my_bonus would be (2, 0, 0)

        valid_saves = list('fort', 'ref', 'will')

        def calc_save(save, level):
            if save not in valid_saves:
                print("Error, not a save value")
                return 0
            else:
                result = {}
                for i in range(1, 4):
                    my_dict = dict(valid_saves[i], int((level / my_mod[i]) + my_bonus[i]))
                    result.append(my_dict)
                return result
        return calc_save  # now you can get some closure

    def get_spells_mod(my_mod):
        def calc_mod(my_mod):
            print("not implemented yet")  # TODO: implement this
        return calc_mod


class Barbarian(Char_Class):
    def __init__(self, master):

        self.class_skill_list = [
            "Acrobatics", "Climb", "Craft",
            "Handle Animal", "Intimidate", "Knowledge: Nature",
            "Perception", "Ride", "Survival", "Swim"]

        self.hit_die = [2, 10]
        self.save_mods = Char_Class.get_save_mod((2.0, 3.0, 4.0), (2, 0, 0))

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
    def __init__(self, master):
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
    def __init__(self, master):
        self.class_skill_list = [
            "Appraise", "Craft", "Diplomacy", "Heal", "Knowledge: Arcana",
            "Knowledge: History", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Profession", "Sense Motive",
            "Spellcraft"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Druid(Char_Class):
    def __init__(self, master):
        self.class_skill_list = [
            "Climb", "Craft", "Fly", "Handle Animal", "Heal",
            "Knowledge: Geography", "Knowledge: Nature",
            "Perception", "Profession", "Ride", "Spellcraft",
            "Survival", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Fighter(Char_Class):
    def __init__(self, master):
        self.class_skill_list = [
            "Climb", "Craft", "Handle Animal", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Engineering", "Profession",
            "Ride", "Survival", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Monk(Char_Class):
    def __init__(self, master):
        self.class_skill_list = [
            "Acrobatics", "Climb", "Craft", "Escape Artist", "Intimidate",
            "Knowledge: History", "Knowledge: Religion", "Perception",
            "Perform", "Profession", "Ride", "Sense Motive",
            "Stealth", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Paladin(Char_Class):
    def __init__(self, master):
        self.class_skill_list = [
            "Craft", "Diplomacy", "Handle Animal", "Heal",
            "Knowledge: Nobility", "Knowledge: Religion",
            "Profession", "Ride", "Sense Motive", "Spellcraft"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Ranger(Char_Class):
    def __init__(self, master):
        self.class_skill_list = [
            "Climb", "Craft", "Handle Animal", "Heal", "Heal", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Geography",
            "Knowledge: Nature", "Perception", "Profession", "Ride",
            "Spellcraft", "Stealth", "Survival", "Swim"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Rogue(Char_Class):
    def __init__(self, master):
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
    def __init__(self, master):
        self.class_skill_list = [
            "Appraise", "Bluff", "Craft", "Fly", "Intimidate",
            "Knowledge: Arcana", "Profession", "Spellcraft",
            "Use Magic Device"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")


class Wizard(Char_Class):
    def __init__(self, master):
        self.class_skill_list = [
            "Appraise", "Craft", "Fly", "Knowledge: Arcana",
            "Knowledge: Dungeoneering", "Knowledge: Engineering",
            "Knowledge: Geography", "Knowledge: History", "Knowledge: Local",
            "Knowledge: Nature", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Profession", "Spellcraft"]

    def make(character):
        character.class_skills = self.class_skill_list
        print("test")
