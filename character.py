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

import random

class character:

    # abilities
    str_mod = 0
    dex_mod = 0
    con_mod = 0
    int_mod = 0
    wis_mod = 0
    cha_mod = 0

    # attributes
    gender = 'none'
    race = 'none'
    size = 'none'
    age = 0
    height = 0
    weight = 0
    hair = 'none'
    eyes = 'none'
    alignment = 'none'

    # modifiers
    fortitude = 0
    fortMagicMod = 0
    fortMiscMod = 0
    reflex = 0
    reflexMagicMod = 0
    reflexMiscMod = 0
    will = 0
    willMagicMod = 0
    willMiscMod = 0

    bab = 0
    spellResist = 0
    ac = 10
    acTouch = 0
    acFlat = 0
    speed = 0
    initiative = 0
    hp = 0
    armorBonus = 0
    shield_bonus = 0
    dodge_bonus = 0
    size_mod = 0
    natural_armor = 0
    deflection_mod = 0
    misc_armor_mod = 0
    cmb = 0
    cmd = 10
    class_skills = None
    skills = None
    numFeats = 0
    feats = None
    Spells = None
    languages = None
    isCaster = False
    spell_failure = 0
    char_class = None
    character_level = 1
    favored_hp = True
    build = 'Random'

    def __init__(self, master):
        self.str = self.setAbilityStat()
        self.dex = self.setAbilityStat()
        self.con = self.setAbilityStat()
        self.int = self.setAbilityStat()
        self.wis = self.setAbilityStat()
        self.cha = self.setAbilityStat()

    def setAbilityStat(self):
        tmp = []
        for i in range(4):
            tmp.append(self.rollDie(6))
        tmp.sort(reverse=True)
        tmp.pop()
        result = 0
        for i in tmp:
            result += i
        return result

    def rollDie(self, sides):
        try:
            random.seed(random.seed(random.random))
            return random.randrange(1, sides+1)
        except ValueError:
            print("Error, invalid number of sides")
