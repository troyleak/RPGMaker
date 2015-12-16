"""
Adds the item to the character object and changes attributes based on the form
"""

class Weapon(Character):
    # Adds a weapon object to a character
    # takes a character object and a weapon object
    def __init__:
        weapon = {'name':"" ,
                'attack_bonus':0 ,
                'critical':0 ,
                'dmg_type':0 ,
                'wpn_range':0 ,
                'ammunition':0 ,
                'damage':"" }

    def add_weapon(character, weapon):
        character.weapons += weapon



class Armor(Character):
    # Adds an armor object to a character
    def add_armor(character, armor):
        character.armor += armor



class Gear(Character):
    # adds a gear object to a character
    def add_gear(character, gear):
        character.gear += gear
