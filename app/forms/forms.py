# from flask_wtf import Form
from wtforms.validators import NumberRange, Optional
from wtforms import StringField as strf, IntegerField as intf
from wtforms import Form, FormField, SubmitField

'''
TODO: Finish validate input
      Plug frontend into backend
Originally intended to use flask_wtf for this, however due to a bug in
CSRF token handling with nested formfields, I'm using the default wtform lib
'''


class WTF_Attributes(Form):
    name = strf(u'Name')
    level = intf(u'Level', [NumberRange(0, 20), Optional()])
    player = strf(u'Player')
    gender = strf(u'Gender')
    race = strf(u'Race')
    size = strf(u'Size')
    age = strf(u'Age')
    height = intf(u'Height (cm)', [NumberRange(0, 300), Optional()])
    weight = intf(u'Weight (kg)', [NumberRange(0, 300), Optional()])
    hair = strf(u'Hair')
    eyes = strf(u'Eyes')
    alignment = strf(u'Alignment')
    deity = strf(u'Deity')
    homeland = strf(u'Homeland')
    char_class = strf(u'Class')


class WTF_Abilities(Form):

    strength = intf(u'Strength', [NumberRange(0, 21), Optional()])
    dexterity = intf(u'Dexterity', [NumberRange(0, 21), Optional()])
    constitution = intf(u'Constitution', [NumberRange(0, 21), Optional()])
    intelligence = intf(u'Intelligence', [NumberRange(0, 21), Optional()])
    wisdom = intf(u'Wisdom', [NumberRange(0, 21), Optional()])
    charisma = intf(u'Charisma', [NumberRange(0, 21), Optional()])


class WTF_Skills(Form):
    acrobatics = intf(u'Acrobatics', [NumberRange(0, 0), Optional()])
    appraise = intf(u'Appraise', [NumberRange(0, 0), Optional()])
    bluff = intf(u'Bluff', [NumberRange(0, 0), Optional()])
    climb = intf(u'Climb', [NumberRange(0, 0), Optional()])
    craft_a = intf(u'Craft a', [NumberRange(0, 0), Optional()])
    craft_b = intf(u'Craft b', [NumberRange(0, 0), Optional()])
    craft_c = intf(u'Craft c', [NumberRange(0, 0), Optional()])
    diplomacy = intf(u'Diplomacy', [NumberRange(0, 0), Optional()])
    disable_device = intf(u'Disable Device', [NumberRange(0, 0), Optional()])
    disguise = intf(u'Disguise', [NumberRange(0, 0), Optional()])
    escape_artist = intf(u'Escape Artist', [NumberRange(0, 0), Optional()])
    fly = intf(u'Fly', [NumberRange(0, 0), Optional()])
    handle_animal = intf(u'Handle Animal', [NumberRange(0, 0), Optional()])
    heal = intf(u'Heal', [NumberRange(0, 0), Optional()])
    intimidate = intf(u'Intimidate', [NumberRange(0, 0), Optional()])
    knowledge_arcana = intf(
                u'Knowledge Arcana', [NumberRange(0, 0), Optional()])
    knowledge_dungeoneering = intf(
                u'Knowledge - Dungeoneering', [NumberRange(0, 0), Optional()])
    knowledge_engineering = intf(
                u'Knowledge - Engineering', [NumberRange(0, 0), Optional()])
    knowledge_geography = intf(
                u'Knowledge - Geography', [NumberRange(0, 0), Optional()])
    knowledge_history = intf(
                u'Knowledge - History', [NumberRange(0, 0), Optional()])
    knowledge_local = intf(
                u'Knowledge - Local', [NumberRange(0, 0), Optional()])
    knowledge_nature = intf(
                u'Knowledge - Nature', [NumberRange(0, 0), Optional()])
    knowledge_nobility = intf(
                u'Knowledge - Nobility', [NumberRange(0, 0), Optional()])
    knowledge_planes = intf(
                u'Knowledge - Planes', [NumberRange(0, 0), Optional()])
    knowledge_religion = intf(
                u'Knowledge - Religion', [NumberRange(0, 0), Optional()])
    linguistics = intf(u'Linguistics', [NumberRange(0, 0), Optional()])
    perception = intf(u'Perception', [NumberRange(0, 0), Optional()])
    perform_a = intf(u'Perform A', [NumberRange(0, 0), Optional()])
    perform_b = intf(u'Perform B', [NumberRange(0, 0), Optional()])
    profession_a = intf(u'Profession A', [NumberRange(0, 0), Optional()])
    profession_b = intf(u'Profession B', [NumberRange(0, 0), Optional()])
    ride = intf(u'Ride', [NumberRange(0, 0), Optional()])
    sense_motive = intf(u'Sense Motive', [NumberRange(0, 0), Optional()])
    sleight_of_hand = intf(u'Sleight of Hand', [NumberRange(0, 0), Optional()])
    spellcraft = intf(u'Spellcraft', [NumberRange(0, 0), Optional()])
    stealth = intf(u'Stealth', [NumberRange(0, 0), Optional()])
    survival = intf(u'Survival', [NumberRange(0, 0), Optional()])
    swim = intf(u'Swim', [NumberRange(0, 0), Optional()])
    use_magic_device = intf(
                u'Use Magic Device', [NumberRange(0, 0), Optional()])


class WTF_Weapon(Form):

    name = strf(u'Name')
    attack_bonus = intf(u'Attack Bonus', [NumberRange(0, 0), Optional()])
    critical = intf(u'Critical', [NumberRange(0, 0), Optional()])
    dmg_type = intf(u'Damage Type', [NumberRange(0, 0), Optional()])
    wpn_range = intf(u'Weapon Range', [NumberRange(0, 0), Optional()])
    ammunition = intf(u'Ammunition', [NumberRange(0, 0), Optional()])
    damage = strf(u'Damage')


class WTF_Armor(Form):

    name = strf(u'Name')
    bonus = intf(u'Bonus', [NumberRange(0, 0), Optional()])
    armor_type = strf(u'Armor Type', [NumberRange(0, 0), Optional()])
    check_penalty = intf(u'Check Penalty', [NumberRange(0, 0), Optional()])
    spell_failure = intf(u'Spell Failure', [NumberRange(0, 0), Optional()])
    weight = intf(u'Weight', [NumberRange(0, 0), Optional()])
    properties = strf(u'Properties')


class WTF_Item(Form):

    item = strf(u'Item')
    weight = intf(u'Weight', [NumberRange(0, 0), Optional()])


class WTF_Charsheet(Form):
    attributes = FormField(WTF_Attributes)
    abilities = FormField(WTF_Abilities)
    skills = FormField(WTF_Skills)
    weapon = FormField(WTF_Weapon)
    armor = FormField(WTF_Armor)
    item = FormField(WTF_Item)
    submit = SubmitField()
