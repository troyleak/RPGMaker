'''
Class Items

Weapons and Armor take a dict containing their stats.

Items do not, they simply take the name, weight, and properties

'''


class Weapon():

    def __init__(self):
        self.weapon = {
            'name': "",
            'attack_bonus': 0,
            'critical': 0,
            'dmg_type': 0,
            'wpn_range': 0,
            'ammunition': 0,
            'damage': ""}

    def make(self, weapon_attributes_list):
        for i in weapon_attributes_list:
            try:
                self.weapon[i] = weapon_attributes_list[i]
            except:
                print("error assigning " + i)


class Armor():

    def __init__(self):
        self.armor = {
            'name': "",
            'armor_bonus': 0,
            'armor_type': "",
            'check_penalty': 0,
            'spell_failure': 0,
            'weight': 0,
            'properties': ""}
        print("Created uninitialized Armor item")

    def make(self, armor_attributes_list):
        for i in armor_attributes_list:
            try:
                self.armor[i] = armor_attributes_list[i]
            except:
                print("error assigning " + i)


class Item():

    def __init__(self):
        self.item = {'name': "",
                     'weight': 0,
                     'properties': ""}
        print("Created uninitialized item")

    def make(self, name, weight, properties):
        self.name = name
        self.weight = weight
        self.properties = properties
        print("Initialized Item")


class Gear():
    # gear is a container for the other itemtypes
    def __init__(self):
        self.weapons = []
        self.armor = []
        self.items = []

    def add_gear(self, gear_type, gear):
        print("Adding " + gear_type + " to gear list")
        if gear_type == "weapon":
            self.weapons.append(gear)
        if gear_type == "armor":
            self.armor.append(gear)
        if gear_type == "item":
            self.items.append(gear)
