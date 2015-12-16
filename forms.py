from flask_wtf import Form
from wtforms import validators
from wtforms import StringField as strf
from wtforms import IntegerField as intf

# TODO: Validate input
#       Plug frontend into backend
#       switch from vanilla CSS to Bootstrap

class WTF_Attributes(Form):
    name = strf(u'name', validators=[validators.Required()])
    level = intf(u'level', validators=[validators.Required(), validators.NumberRange(0, 0)])
    player = strf(u'player', validators=[validators.Required()])
    gender = strf(u'gender', validators=[validators.Required()])
    race = strf(u'race', validators=[validators.Required()])
    size = strf(u'size', validators=[validators.Required()])
    age = strf(u'age', validators=[validators.Required()])
    height = intf(u'height', validators=[validators.Required(), validators.NumberRange(0, 0)])
    weight = intf(u'weight', validators=[validators.Required(), validators.NumberRange(0, 0)])
    hair = strf(u'hair', validators=[validators.Required()])
    eyes = strf(u'eyes', validators=[validators.Required()])
    alignment = strf(u'alignment', validators=[validators.Required()])
    deity = strf(u'deity', validators=[validators.Required()])
    homeland = strf(u'homeland', validators=[validators.Required()])



class WTF_Abilities(Form):

    strength = intf(u'Strength', validators=[validators.Required(), validators.NumberRange(0, 0)])
    dexterity = intf(u'Dexterity', validators=[validators.Required(), validators.NumberRange(0, 0)])
    constitution = intf(u'Constitution', validators=[validators.Required(), validators.NumberRange(0, 0)])
    intelligence = intf(u'Intelligence', validators=[validators.Required(), validators.NumberRange(0, 0)])
    wisdom = intf(u'Wisdom', validators=[validators.Required(), validators.NumberRange(0, 0)])
    charisma = intf(u'Charisma', validators=[validators.Required(), validators.NumberRange(0, 0)])



class WTF_Skills(Form):

    acrobatics = intf(u'acrobatics', validators=[validators.Required(), validators.NumberRange(0, 0)])
    appraise = intf(u'appraise', validators=[validators.Required(), validators.NumberRange(0, 0)])
    bluff = intf(u'bluff', validators=[validators.Required(), validators.NumberRange(0, 0)])
    climb = intf(u'climb', validators=[validators.Required(), validators.NumberRange(0, 0)])
    craft_a = intf(u'craft a', validators=[validators.Required(), validators.NumberRange(0, 0)])
    craft_b = intf(u'craft b', validators=[validators.Required(), validators.NumberRange(0, 0)])
    craft_c = intf(u'craft c', validators=[validators.Required(), validators.NumberRange(0, 0)])
    diplomacy = intf(u'diplomacy', validators=[validators.Required(), validators.NumberRange(0, 0)])
    disable_device = intf(u'disable device', validators=[validators.Required(), validators.NumberRange(0, 0)])
    disguise = intf(u'disguise', validators=[validators.Required(), validators.NumberRange(0, 0)])
    escape_artist = intf(u'escape artist', validators=[validators.Required(), validators.NumberRange(0, 0)])
    fly = intf(u'fly', validators=[validators.Required(), validators.NumberRange(0, 0)])
    handle_animal = intf(u'handle animal', validators=[validators.Required(), validators.NumberRange(0, 0)])
    heal = intf(u'heal', validators=[validators.Required(), validators.NumberRange(0, 0)])
    intimidate = intf(u'intimidate', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_arcana = intf(u'knowledge arcana', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_dungeoneering = intf(u'knowledge dungeoneering', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_engineering = intf(u'knowledge engineering', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_geography = intf(u'knowledge geography', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_history = intf(u'knowledge history', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_local = intf(u'knowledge local', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_nature = intf(u'knowledge nature', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_nobility = intf(u'knowledge nobility', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_planes = intf(u'knowledge planes', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_religion = intf(u'knowledge religion', validators=[validators.Required(), validators.NumberRange(0, 0)])
    linguistics = intf(u'linguistics', validators=[validators.Required(), validators.NumberRange(0, 0)])
    perception = intf(u'perception', validators=[validators.Required(), validators.NumberRange(0, 0)])
    perform_a = intf(u'perform a', validators=[validators.Required(), validators.NumberRange(0, 0)])
    perform_b = intf(u'perform b', validators=[validators.Required(), validators.NumberRange(0, 0)])
    profession_a = intf(u'profession a', validators=[validators.Required(), validators.NumberRange(0, 0)])
    profession_b = intf(u'profession b', validators=[validators.Required(), validators.NumberRange(0, 0)])
    ride = intf(u'ride', validators=[validators.Required(), validators.NumberRange(0, 0)])
    sense_motive = intf(u'sense motive', validators=[validators.Required(), validators.NumberRange(0, 0)])
    sleight_of_hand = intf(u'sleight of hand', validators=[validators.Required(), validators.NumberRange(0, 0)])
    spellcraft = intf(u'spellcraft', validators=[validators.Required(), validators.NumberRange(0, 0)])
    stealth = intf(u'stealth', validators=[validators.Required(), validators.NumberRange(0, 0)])
    survival = intf(u'survival', validators=[validators.Required(), validators.NumberRange(0, 0)])
    swim = intf(u'swim', validators=[validators.Required(), validators.NumberRange(0, 0)])
    use_magic_device = intf(u'use magic device', validators=[validators.Required(), validators.NumberRange(0, 0)])



class WTF_Weapon(Form):

    name = strf(u'name', validators=[validators.Required()])
    attack_bonus = intf(u'attack bonus', validators=[validators.Required(), validators.NumberRange(0, 0)])
    critical = intf(u'critical', validators=[validators.Required(), validators.NumberRange(0, 0)])
    dmg_type = intf(u'damage type', validators=[validators.Required(), validators.NumberRange(0, 0)])
    wpn_range = intf(u'weapon range', validators=[validators.Required(), validators.NumberRange(0, 0)])
    ammunition = intf(u'ammunition', validators=[validators.Required(), validators.NumberRange(0, 0)])
    damage = strf(u'damage', validators=[validators.Required()])



class WTF_Armor(Form):

    name = strf(u'name', validators=[validators.Required()])
    bonus = intf(u'bonus', validators=[validators.Required(), validators.NumberRange(0, 0)])
    armor_type = strf(u'armor type', validators=[validators.Required(), validators.NumberRange(0, 0)])
    check_penalty = intf(u'check penalty', validators=[validators.Required(), validators.NumberRange(0, 0)])
    spell_failure = intf(u'spell failure', validators=[validators.Required(), validators.NumberRange(0, 0)])
    weight = intf(u'weight', validators=[validators.Required(), validators.NumberRange(0, 0)])
    properties = strf(u'properties', validators=[validators.Required()])



class WTF_Item(Form):

    item = strf(u'item', validators=[validators.Required()])
    weight = intf(u'weight', validators=[validators.Required(), validators.NumberRange(0, 0)])
