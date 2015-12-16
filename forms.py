from flask_wtf import Form
from wtforms import validators
from wtforms import StringField as strf
from wtforms import IntegerField as intf



class WTF_Attributes(Form):
    name = strf(u'name', validators=[validators.input_required()])
    level = strf(u'level', validators=[validators.input_required()])
    player = strf(u'player', validators=[validators.input_required()])
    gender = strf(u'gender', validators=[validators.input_required()])
    race = strf(u'race', validators=[validators.input_required()])
    size = strf(u'size', validators=[validators.input_required()])
    age = strf(u'age', validators=[validators.input_required()])
    height = strf(u'height', validators=[validators.input_required()])
    weight = strf(u'weight', validators=[validators.input_required()])
    hair = strf(u'hair', validators=[validators.input_required()])
    eyes = strf(u'eyes', validators=[validators.input_required()])
    alignment = strf(u'alignment', validators=[validators.input_required()])
    deity = strf(u'deity', validators=[validators.input_required()])
    homeland = strf(u'homeland', validators=[validators.input_required()])



class WTF_Abilities(Form):

    strength = strf(u'Strength', validators=[validators.input_required()])
    dexterity = strf(u'Dexterity', validators=[validators.input_required()])
    constitution = strf(u'Constitution', validators=[validators.input_required()])
    intelligence = strf(u'Intelligence', validators=[validators.input_required()])
    wisdom = strf(u'Wisdom', validators=[validators.input_required()])
    charisma = strf(u'Charisma', validators=[validators.input_required()])



class WTF_Skills(Form):
    acrobatics = strf(u'acrobatics', validators=[validators.input_required()])
    appraise = strf(u'appraise', validators=[validators.input_required()])
    bluff = strf(u'bluff', validators=[validators.input_required()])
    climb = strf(u'climb', validators=[validators.input_required()])
    craft_a = strf(u'craft a', validators=[validators.input_required()])
    craft_b = strf(u'craft b', validators=[validators.input_required()])
    craft_c = strf(u'craft c', validators=[validators.input_required()])
    diplomacy = strf(u'diplomacy', validators=[validators.input_required()])
    disable_device = strf(u'disable device', validators=[validators.input_required()])
    disguise = strf(u'disguise', validators=[validators.input_required()])
    escape_artist = strf(u'escape artist', validators=[validators.input_required()])
    fly = strf(u'fly', validators=[validators.input_required()])
    handle_animal = strf(u'handle animal', validators=[validators.input_required()])
    heal = strf(u'heal', validators=[validators.input_required()])
    intimidate = strf(u'intimidate', validators=[validators.input_required()])
    knowledge_arcana = strf(u'knowledge arcana', validators=[validators.input_required()])
    knowledge_dungeoneering = strf(u'knowledge dungeoneering', validators=[validators.input_required()])
    knowledge_engineering = strf(u'knowledge engineering', validators=[validators.input_required()])
    knowledge_geography = strf(u'knowledge geography', validators=[validators.input_required()])
    knowledge_history = strf(u'knowledge history', validators=[validators.input_required()])
    knowledge_local = strf(u'knowledge local', validators=[validators.input_required()])
    knowledge_nature = strf(u'knowledge nature', validators=[validators.input_required()])
    knowledge_nobility = strf(u'knowledge nobility', validators=[validators.input_required()])
    knowledge_planes = strf(u'knowledge planes', validators=[validators.input_required()])
    knowledge_religion = strf(u'knowledge religion', validators=[validators.input_required()])
    linguistics = strf(u'linguistics', validators=[validators.input_required()])
    perception = strf(u'perception', validators=[validators.input_required()])
    perform_a = strf(u'perform a', validators=[validators.input_required()])
    perform_b = strf(u'perform b', validators=[validators.input_required()])
    profession_a = strf(u'profession a', validators=[validators.input_required()])
    profession_b = strf(u'profession b', validators=[validators.input_required()])
    ride = strf(u'ride', validators=[validators.input_required()])
    sense_motive = strf(u'sense motive', validators=[validators.input_required()])
    sleight_of_hand = strf(u'sleight of hand', validators=[validators.input_required()])
    spellcraft = strf(u'spellcraft', validators=[validators.input_required()])
    stealth = strf(u'stealth', validators=[validators.input_required()])
    survival = strf(u'survival', validators=[validators.input_required()])
    swim = strf(u'swim', validators=[validators.input_required()])
    use_magic_device = strf(u'use magic device', validators=[validators.input_required()])



class WTF_Weapon(Form):
    name = strf(u'name', validators=[validators.input_required()])
    attack_bonus = strf(u'attack bonus', validators=[validators.input_required()])
    critical = strf(u'critical', validators=[validators.input_required()])
    dmg_type = strf(u'damage type', validators=[validators.input_required()])
    wpn_range = strf(u'weapon range', validators=[validators.input_required()])
    ammunition = strf(u'ammunition', validators=[validators.input_required()])
    damage = strf(u'damage', validators=[validators.input_required()])



class WTF_Armor(Form):
    name = strf(u'name', validators=[validators.input_required()])
    bonus = strf(u'bonus', validators=[validators.input_required()])
    armor_type = strf(u'armor type', validators=[validators.input_required()])
    check_penalty = strf(u'check penalty', validators=[validators.input_required()])
    spell_failure = strf(u'spell failure', validators=[validators.input_required()])
    weight = strf(u'weight', validators=[validators.input_required()])
    properties = strf(u'properties', validators=[validators.input_required()])



class WTF_Item(Form):
    item = strf(u'item', validators=[validators.input_required()])
    weight = strf(u'weight', validators=[validators.input_required()])
