"""
Adds the item to the character object and changes attributes based on the form
"""

class Weapon():
    # Adds a weapon object to a character
    # takes a character object and a weapon object
    def __init__():
        weapon = {'name':"" ,
                'attack_bonus':0 ,
                'critical':0 ,
                'dmg_type':0 ,
                'wpn_range':0 ,
                'ammunition':0 ,
                'damage':"" }

    def add_weapon(character, weapon):
        character.weapons += weapon



class Armor():
    # Adds an armor object to a character
    def __init__():
        armor = {'name':"" ,
                'armor_bonus':0 ,
                'type':"" ,
                'check_penalty':0 ,
                'spell_failure':0 ,
                'weight':0 ,
                'properties':"" }

    def add_armor(character, armor):
        character.armor += armor



class Gear():
    # adds a gear object to a character
    def __init__():
        gear = {'name':"" ,
                'weight':0 }

    def add_gear(character, gear):
        character.gear += gear
