from collections import namedtuple
from . import dice


'''
Abilities

This class contains values pertaining to ability scores.
It defines an Ability namedtuple containing the stat and modifier

To change the stats, you'll need to replace the existing namedtuple object with
a new one. Maybe that will change later

'''

class Abilities():

    def __init__(self):

        self.valid_stats = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

        self.strength = 10
        self.strength_mod = 0

        self.dexterity = 10
        self.dexterity_mod = 0

        self.constitution = 10
        self.constitution_mod = 0

        self.intelligence = 10
        self.intelligence_mod = 0

        self.wisdom = 10
        self.wisdom_mod = 0

        self.charisma = 10
        self.charisma_mod = 0

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



    def set_scores(self, str_, dex_, con_, int_, wis_, cha_):
        self.strength = Ability(str_, set_ability_mod(str_) )
        self.dexterity = Ability(dex_, set_ability_mod(dex_) )
        self.constitution = Ability(con_, set_ability_mod(con_) )
        self.intelligence = Ability(int_, set_ability_mod(int_) )
        self.wisdom = Ability(wis_, set_ability_mod(wis_) )
        self.charisma = Ability(cha_, set_ability_mod(cha_) )



    def set_ability_stat_rand(self, stat):
        # Sets the specified stat to a random value using the roll 4 drop 1 method
        lst = dice.Dice.roll_dice(6, 4)
        result = sum(dice.Dice.drop_lowest(lst))
        self.stat = result
        print("setting " + str(stat) + " to " + str(result))
        return result



    def set_ability_mod(stat):
        # returns the ability modifier for a given stat
        if stat >= 10:
            modifier = (stat - 10) / 2
        elif stat < 10:
            modifier = (11 - stat) / 2 * -1
        return modifier



    def get_ability_scores(self):
        return [self.strength, self.dexterity, self.constitution,
                self.intelligence, self.wisdom, self.charisma]



    def get_ability_mods(self):
        return [self.strength_mod, self.dexterity_mod, self.constitution_mod,
                self.intelligence_mod, self.wisdom_mod, self.charisma_mod]
