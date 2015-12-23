from collections import namedtuple

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

        Ability = namedtuple('Ability', ['stat', 'mod'])

        self.strength = Ability(10, 0)
        self.dexterity = Ability(10, 0)
        self.constitution = Ability(10, 0)
        self.intelligence = Ability(10, 0)
        self.wisdom = Ability(10, 0)
        self.charisma = Ability(10, 0)

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


    def set_ability_stat_rand(self):
        lst = []
        for i in range(4):
            tmp = super.roll_die(self, 6) # use roll_die in character for portability
            lst.append(tmp)
        lst.sort(reverse=True)
        lst.pop()
        result = 0
        for i in lst:
            result += i
        return result

    def set_ability_mod(self, stat):
        # returns the ability modifier for a given stat
        if stat >= 10:
            modifier = (stat - 10) / 2
        elif stat < 10:
            modifier = (11 - stat) / 2 * -1
        return modifier

    def get_ability_scores(self):
        for i in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            ability_score_list.append(self.i[stat])
        return ability_score_list

    def get_ability_mods(self):
        for i in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
            ability_score_list.append(self.i[mod])
        return ability_score_list
