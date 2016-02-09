from . import dice


'''
Abilities

'''


class Abilities():

    def __init__(self):

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
        for i in self.stats.keys():
            try:
                self.stats[i] = labeled_stats_to_assign[i]
            except:
                print("Error assigning stat " + str(i))

            try:
                self.mods[i] = self.set_ability_mod(self.stats[i])
            except:
                print("Error assigning mod " + str(i))

    def set_ability_stat_rand(self, stat):
        # Sets the specified stat to a random value
        # using the roll 4 drop 1 method
        self.stats[stat] = sum(i for i in dice.Dice.roll_dice(6, 4))

    def set_ability_mod(self, stat):
        # returns the ability modifier for a given stat
        if stat >= 10:
            stat = (stat - 10) / 2
        elif stat < 10:
            stat = (11 - stat) / 2 * -1
        return int(stat)

    def get_ability_scores(self):
        return self.stats

    def get_ability_mods(self):
        return self.mods

    def get_saving_throws(self):
        return [self.fortitude, self.reflex, self.will]
