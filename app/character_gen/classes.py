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

            elif char_class == 'bard':
                master.char_class = Bard()

            elif char_class == 'cleric':
                master.char_class = Cleric()

            elif char_class == 'druid':
                master.char_class = Druid()

            elif char_class == 'fighter':
                master.char_class = Fighter()

            elif char_class == 'monk':
                master.char_class = Monk()

            elif char_class == 'paladin':
                master.char_class = Paladin()

            elif char_class == 'ranger':
                master.char_class = Ranger()

            elif char_class == 'rogue':
                master.char_class = Rogue()

            elif char_class == 'sorcerer':
                master.char_class = Sorcerer()

            elif char_class == 'wizard':
                master.char_class = Wizard()

    def calc_bab(self, level):
        # Takes a level, returns a list of Base Attack Bonuses for it
        value = []

        while (level > 0):
            value.append(level)
            level -= 5  # Breaks loop before appending if level < 5
        value.sort()
        return value

    def calc_save(my_mod, my_bonus):
        valid_saves = ['fort', 'ref', 'will']
        result = []
        for i in valid_saves:
            tmp = int((1 / my_mod[i]) + my_bonus[i])
            result.append(tmp)
        return result


class Barbarian(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Acrobatics", "Climb", "Craft",
            "Handle Animal", "Intimidate", "Knowledge: Nature",
            "Perception", "Ride", "Survival", "Swim"]

        self.hit_die = {
            'sides': 12
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 2.0,
            'ref': 3.0,
            'will': 3.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 2,
            'ref': 0,
            'will': 0
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)

    # Special Abilities by level
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


class Bard(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Acrobatics", "Appraise", "Bluff", "Climb", "Diplomacy",
            "Disguise", "Escape Artist", "Intimidate", "Knowledge: Arcana",
            "Knowledge: Dungeoneering", "Knowledge: Engineering",
            "Knowledge: Geography", "Knowledge: History", "Knowledge: Local",
            "Knowledge: Nature", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Perception", "Perform",
            "Profession", "Sense Motive", "Sleight of Hand", "Spellcraft",
            "Stealth", "Use Magic Device"]

        self.hit_die = {
            'sides': 8
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 3.0,
            'ref': 2.0,
            'will': 2.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 0,
            'ref': 2,
            'will': 2
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Cleric(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Appraise", "Craft", "Diplomacy", "Heal", "Knowledge: Arcana",
            "Knowledge: History", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Profession", "Sense Motive",
            "Spellcraft"]

        self.hit_die = {
            'sides': 8
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 2.0,
            'ref': 3.0,
            'will': 2.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 2,
            'ref': 0,
            'will': 2
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Druid(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Climb", "Craft", "Fly", "Handle Animal", "Heal",
            "Knowledge: Geography", "Knowledge: Nature",
            "Perception", "Profession", "Ride", "Spellcraft",
            "Survival", "Swim"]

        self.hit_die = {
            'sides': 8
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 2.0,
            'ref': 3.0,
            'will': 2.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 2,
            'ref': 0,
            'will': 2
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Fighter(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Climb", "Craft", "Handle Animal", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Engineering", "Profession",
            "Ride", "Survival", "Swim"]

        self.hit_die = {
            'sides': 10
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 2.0,
            'ref': 3.0,
            'will': 3.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 2,
            'ref': 0,
            'will': 0
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Monk(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Acrobatics", "Climb", "Craft", "Escape Artist", "Intimidate",
            "Knowledge: History", "Knowledge: Religion", "Perception",
            "Perform", "Profession", "Ride", "Sense Motive",
            "Stealth", "Swim"]

        self.hit_die = {
            'sides': 8
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 2.0,
            'ref': 2.0,
            'will': 2.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 2,
            'ref': 2,
            'will': 2
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Paladin(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Craft", "Diplomacy", "Handle Animal", "Heal",
            "Knowledge: Nobility", "Knowledge: Religion",
            "Profession", "Ride", "Sense Motive", "Spellcraft"]

        self.hit_die = {
            'sides': 10
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 2.0,
            'ref': 3.0,
            'will': 2.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 2,
            'ref': 0,
            'will': 2
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Ranger(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Climb", "Craft", "Handle Animal", "Heal", "Heal", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Geography",
            "Knowledge: Nature", "Perception", "Profession", "Ride",
            "Spellcraft", "Stealth", "Survival", "Swim"]

        self.hit_die = {
            'sides': 10
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 2.0,
            'ref': 2.0,
            'will': 3.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 2,
            'ref': 2,
            'will': 0
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Rogue(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Acrobatics", "Appraise", "Bluff", "Climb", "Craft", "Diplomacy",
            "Disable Device", "Disguise", "Escape Artist", "Intimidate",
            "Knowledge: Dungeoneering", "Knowledge: Local",
            "Linguistics", "Perception", "Perform",
            "Profession", "Sense Motive", "Sleight of Hand", "Stealth",
            "Swim", "Use Magic Device"]

        self.hit_die = {
            'sides': 8
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 3.0,
            'ref': 2.0,
            'will': 3.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 0,
            'ref': 2,
            'will': 0
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Sorcerer(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Appraise", "Bluff", "Craft", "Fly", "Intimidate",
            "Knowledge: Arcana", "Profession", "Spellcraft",
            "Use Magic Device"]

        self.hit_die = {
            'sides': 6
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 3.0,
            'ref': 3.0,
            'will': 2.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 0,
            'ref': 0,
            'will': 2
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)


class Wizard(Char_Class):
    def __init__(self):
        Char_Class.__init__(self)
        self.class_skill_list = [
            "Appraise", "Craft", "Fly", "Knowledge: Arcana",
            "Knowledge: Dungeoneering", "Knowledge: Engineering",
            "Knowledge: Geography", "Knowledge: History", "Knowledge: Local",
            "Knowledge: Nature", "Knowledge: Nobility", "Knowledge: Planes",
            "Knowledge: Religion", "Linguistics", "Profession", "Spellcraft"]

        self.hit_die = {
            'sides': 6
            }
        self.save_mods = {
            # describes the interval at which each throw increases
            'fort': 3.0,
            'ref': 3.0,
            'will': 2.0
            }
        self.save_bonus = {
            # describes any values that start off ahead of others
            'fort': 0,
            'ref': 0,
            'will': 2
            }
        self.save_throws = Char_Class.calc_save(self.save_mods, self.save_bonus)
