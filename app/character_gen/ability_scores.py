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

        self.valid_stats = ['strength', 'dexterity', 'constitution',
                            'intelligence', 'wisdom', 'charisma']

        self.stats = {'strength': 10, 'dexterity': 10, 'constitution': 10,
                      'intelligence': 10, 'wisdom': 10, 'charisma': 10}

        self.mods = {'strength': 0, 'dexterity': 0, 'constitution': 0,
                     'intelligence': 0, 'wisdom': 0, 'charisma': 0}

        # Saving throws and modifiers
        self.fortitude = {'stat': 0, 'magic_mod': 0, 'misc_mod': 0}
        self.reflex = {'stat': 0, 'magic_mod': 0, 'misc_mod': 0}
        self.will = {'stat': 0, 'magic_mod': 0, 'misc_mod': 0}

    def set_ability_scores(self, labeled_stats_to_assign):
        # takes a dict of stats to assign and their values
        for i in self.valid_stats:
            try:
                self.stats[i] = labeled_stats_to_assign[i]
            except:
                print("Error assigning stat " + str(i))

    def set_ability_stat_rand(self, stat):
        # Sets the specified stat to a random value
        # using the roll 4 drop 1 method
        lst = dice.Dice.roll_dice(6, 4)
        result = sum(dice.Dice.drop_lowest(lst))
        self.stat = result
        return result

    def set_ability_mod(self, stat):
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
