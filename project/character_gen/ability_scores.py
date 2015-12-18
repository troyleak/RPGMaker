from collections import namedtuple

'''
Abilities

This class contains values pertaining to ability scores.
It defines an Ability namedtuple containing the stat and modifier

To change the stats, you'll need to replace the existing namedtuple object with
a new one. Maybe that will change later

'''

class Abilities():
    def __init__():
        Ability = namedtuple('Ability', ['stat', 'mod'])

        self.strength = Ability(0, 0)
        self.dexterity = Ability(0, 0)
        self.constitution = Ability(0, 0)
        self.intelligence = Ability(0, 0)
        self.wisdom = Ability(0, 0)
        self.charisma = Ability(0, 0)

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
