# from flask_wtf import Form
from wtforms import validators
from wtforms import Form, StringField as strf, IntegerField as intf, FormField, SubmitField

# TODO: Finish validate input
#       Plug frontend into backend

# Originally intended to use flask_wtf for this, however due to a bug in
# CSRF token handling with nested formfields, I'm using the default wtform lib

class WTF_Attributes(Form):
    name = strf(u'Name')
    level = intf(u'Level', validators=[validators.NumberRange(0, 0)])
    player = strf(u'Player')
    gender = strf(u'Gender')
    race = strf(u'Race')
    size = strf(u'Size')
    age = strf(u'Age')
    height = intf(u'Height', validators=[validators.NumberRange(0, 0)])
    weight = intf(u'Weight', validators=[validators.NumberRange(0, 0)])
    hair = strf(u'Hair')
    eyes = strf(u'Eyes')
    alignment = strf(u'Alignment')
    deity = strf(u'Deity')
    homeland = strf(u'Homeland')



class WTF_Abilities(Form):

    strength = intf(u'Strength', validators=[validators.NumberRange(0, 0)])
    dexterity = intf(u'Dexterity', validators=[validators.NumberRange(0, 0)])
    constitution = intf(u'Constitution', validators=[validators.NumberRange(0, 0)])
    intelligence = intf(u'Intelligence', validators=[validators.NumberRange(0, 0)])
    wisdom = intf(u'Wisdom', validators=[validators.NumberRange(0, 0)])
    charisma = intf(u'Charisma', validators=[validators.NumberRange(0, 0)])



class WTF_Skills(Form):

    acrobatics = intf(u'Acrobatics', validators=[validators.NumberRange(0, 0)])
    appraise = intf(u'Appraise', validators=[validators.NumberRange(0, 0)])
    bluff = intf(u'Bluff', validators=[validators.NumberRange(0, 0)])
    climb = intf(u'Climb', validators=[validators.NumberRange(0, 0)])
    craft_a = intf(u'Craft a', validators=[validators.NumberRange(0, 0)])
    craft_b = intf(u'Craft b', validators=[validators.NumberRange(0, 0)])
    craft_c = intf(u'Craft c', validators=[validators.NumberRange(0, 0)])
    diplomacy = intf(u'Diplomacy', validators=[validators.NumberRange(0, 0)])
    disable_device = intf(u'Disable Device', validators=[validators.NumberRange(0, 0)])
    disguise = intf(u'Disguise', validators=[validators.NumberRange(0, 0)])
    escape_artist = intf(u'Escape Artist', validators=[validators.NumberRange(0, 0)])
    fly = intf(u'Fly', validators=[validators.NumberRange(0, 0)])
    handle_animal = intf(u'Handle Animal', validators=[validators.NumberRange(0, 0)])
    heal = intf(u'Heal', validators=[validators.NumberRange(0, 0)])
    intimidate = intf(u'Intimidate', validators=[validators.NumberRange(0, 0)])
    knowledge_arcana = intf(u'Knowledge Arcana', validators=[validators.NumberRange(0, 0)])
    knowledge_dungeoneering = intf(u'Knowledge - Dungeoneering', validators=[validators.NumberRange(0, 0)])
    knowledge_engineering = intf(u'Knowledge - Engineering', validators=[validators.NumberRange(0, 0)])
    knowledge_geography = intf(u'Knowledge - Geography', validators=[validators.NumberRange(0, 0)])
    knowledge_history = intf(u'Knowledge - History', validators=[validators.NumberRange(0, 0)])
    knowledge_local = intf(u'Knowledge - Local', validators=[validators.NumberRange(0, 0)])
    knowledge_nature = intf(u'Knowledge - Nature', validators=[validators.NumberRange(0, 0)])
    knowledge_nobility = intf(u'Knowledge - Nobility', validators=[validators.NumberRange(0, 0)])
    knowledge_planes = intf(u'Knowledge - Planes', validators=[validators.NumberRange(0, 0)])
    knowledge_religion = intf(u'Knowledge - Religion', validators=[validators.NumberRange(0, 0)])
    linguistics = intf(u'Linguistics', validators=[validators.NumberRange(0, 0)])
    perception = intf(u'Perception', validators=[validators.NumberRange(0, 0)])
    perform_a = intf(u'Perform A', validators=[validators.NumberRange(0, 0)])
    perform_b = intf(u'Perform B', validators=[validators.NumberRange(0, 0)])
    profession_a = intf(u'Profession A', validators=[validators.NumberRange(0, 0)])
    profession_b = intf(u'Profession B', validators=[validators.NumberRange(0, 0)])
    ride = intf(u'Ride', validators=[validators.NumberRange(0, 0)])
    sense_motive = intf(u'Sense Motive', validators=[validators.NumberRange(0, 0)])
    sleight_of_hand = intf(u'Sleight of Hand', validators=[validators.NumberRange(0, 0)])
    spellcraft = intf(u'Spellcraft', validators=[validators.NumberRange(0, 0)])
    stealth = intf(u'Stealth', validators=[validators.NumberRange(0, 0)])
    survival = intf(u'Survival', validators=[validators.NumberRange(0, 0)])
    swim = intf(u'Swim', validators=[validators.NumberRange(0, 0)])
    use_magic_device = intf(u'Use Magic Device', validators=[validators.NumberRange(0, 0)])



class WTF_Weapon(Form):

    name = strf(u'Name')
    attack_bonus = intf(u'Attack Bonus', validators=[validators.NumberRange(0, 0)])
    critical = intf(u'Critical', validators=[validators.NumberRange(0, 0)])
    dmg_type = intf(u'Damage Type', validators=[validators.NumberRange(0, 0)])
    wpn_range = intf(u'Weapon Range', validators=[validators.NumberRange(0, 0)])
    ammunition = intf(u'Ammunition', validators=[validators.NumberRange(0, 0)])
    damage = strf(u'Damage')



class WTF_Armor(Form):

    name = strf(u'Name')
    bonus = intf(u'Bonus', validators=[validators.NumberRange(0, 0)])
    armor_type = strf(u'Armor Type', validators=[validators.NumberRange(0, 0)])
    check_penalty = intf(u'Check Penalty', validators=[validators.NumberRange(0, 0)])
    spell_failure = intf(u'Spell Failure', validators=[validators.NumberRange(0, 0)])
    weight = intf(u'Weight', validators=[validators.NumberRange(0, 0)])
    properties = strf(u'Properties')



class WTF_Item(Form):

    item = strf(u'Item')
    weight = intf(u'Weight', validators=[validators.NumberRange(0, 0)])


class WTF_Charsheet(Form):
    attributes = FormField(WTF_Attributes)
    abilities = FormField(WTF_Abilities)
    skills = FormField(WTF_Skills)
    weapon = FormField(WTF_Weapon)
    armor = FormField(WTF_Armor)
    item = FormField(WTF_Item)
    submit = SubmitField('Submit')
