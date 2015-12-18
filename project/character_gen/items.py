'''
Class Items

Contains classes for each type of item the player is capable of carrying
Right now the Gear class is not able to directly modify stats.
That *may* change, but not right now.

To use it, create an Items object and add child objects to it

For example:


    character.items = Items

    weapon = Weapon.make("parameters", "go", "here")

    character.items.add_weapon(weapon)


TODO: Determine if input validation is necessary. If so, do that

'''

class Weapon():

    def __init__(self, master):
        self.weapon = { 'name':"" ,
                        'attack_bonus':0 ,
                        'critical':0 ,
                        'dmg_type':0 ,
                        'wpn_range':0 ,
                        'ammunition':0 ,
                        'damage':"" }
        print("Created uninitialized Weapon item")

    def make(self, name, attack_bonus, critical, dmg_type, wpn_range, ammunition, damage):
        self.name = name
        self.attack_bonus = attack_bonus
        self.critical = critical
        self.dmg_type = dmg_type
        self.wpn_range = wpn_range
        self.ammunition = ammunition
        self.damage = damage
        print("Initialized Weapon")


class Armor():

    def __init__(self, master):
        self.armor =  { 'name':"" ,
                        'armor_bonus':0 ,
                        'armor_type':"" ,
                        'check_penalty':0 ,
                        'spell_failure':0 ,
                        'weight':0 ,
                        'properties':"" }
        print("Created uninitialized Armor item")

    def make(self, name, armor_bonus, armor_type, check_penalty, spell_failure, weight, properties):
        self.name = name
        self.armor_bonus = armor_bonus
        self.type = armor_type
        self.check_penalty = check_penalty
        self.spell_failure = spell_failure
        self.weight = weight
        self.properties = properties
        print("Initialized Armor")


class Gear():

    def __init__(self, master):
        self.gear = {'name':"" ,
                     'weight':0,
                     'properties':"" }
        print("Created uninitialized Gear item")

    def make(self, name, weight, properties):
        self.name = name
        self.weight = weight
        self.properties = properties
        print("Initialized Gear")


class Items():

    def __init__(self, master):
        self.weapons = []
        self.armor = []
        self.gear = []

    def add_weapon(self, weapon):
        self.weapons += weapon


    def add_armor(self, armor):
        self.armor += armor


    def add_gear(self, gear):
        self.gear += gear
