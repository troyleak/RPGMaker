# from flask_wtf import Form
from wtforms.validators import NumberRange, Optional
from wtforms import Form, StringField, IntegerField, FormField, SubmitField

# TODO: Finish validate input
#       Plug frontend into backend

# Originally intended to use flask_wtf for this, however due to a bug in
# CSRF token handling with nested formfields, I'm using the default wtform lib

class WTF_Attributes(Form):
    name = StringField(u'Name')
    level = IntegerField(u'Level', validators=[NumberRange(0, 20), Optional()])
    player = StringField(u'Player')
    gender = StringField(u'Gender')
    race = StringField(u'Race')
    size = StringField(u'Size')
    age = StringField(u'Age')
    height = IntegerField(u'Height (cm)', validators=[NumberRange(0, 300), Optional()])
    weight = IntegerField(u'Weight (kg)', validators=[NumberRange(0, 300), Optional()])
    hair = StringField(u'Hair')
    eyes = StringField(u'Eyes')
    alignment = StringField(u'Alignment')
    deity = StringField(u'Deity')
    homeland = StringField(u'Homeland')
    char_class = StringField(u'Class')


class WTF_Abilities(Form):

    strength = IntegerField(u'Strength', validators=[NumberRange(0, 21), Optional()])
    dexterity = IntegerField(u'Dexterity', validators=[NumberRange(0, 21), Optional()])
    constitution = IntegerField(u'Constitution', validators=[NumberRange(0, 21), Optional()])
    intelligence = IntegerField(u'Intelligence', validators=[NumberRange(0, 21), Optional()])
    wisdom = IntegerField(u'Wisdom', validators=[NumberRange(0, 21), Optional()])
    charisma = IntegerField(u'Charisma', validators=[NumberRange(0, 21), Optional()])



class WTF_Skills(Form):

    acrobatics = IntegerField(u'Acrobatics', validators=[NumberRange(0, 0), Optional()])
    appraise = IntegerField(u'Appraise', validators=[NumberRange(0, 0), Optional()])
    bluff = IntegerField(u'Bluff', validators=[NumberRange(0, 0), Optional()])
    climb = IntegerField(u'Climb', validators=[NumberRange(0, 0), Optional()])
    craft_a = IntegerField(u'Craft a', validators=[NumberRange(0, 0), Optional()])
    craft_b = IntegerField(u'Craft b', validators=[NumberRange(0, 0), Optional()])
    craft_c = IntegerField(u'Craft c', validators=[NumberRange(0, 0), Optional()])
    diplomacy = IntegerField(u'Diplomacy', validators=[NumberRange(0, 0), Optional()])
    disable_device = IntegerField(u'Disable Device', validators=[NumberRange(0, 0), Optional()])
    disguise = IntegerField(u'Disguise', validators=[NumberRange(0, 0), Optional()])
    escape_artist = IntegerField(u'Escape Artist', validators=[NumberRange(0, 0), Optional()])
    fly = IntegerField(u'Fly', validators=[NumberRange(0, 0), Optional()])
    handle_animal = IntegerField(u'Handle Animal', validators=[NumberRange(0, 0), Optional()])
    heal = IntegerField(u'Heal', validators=[NumberRange(0, 0), Optional()])
    intimidate = IntegerField(u'Intimidate', validators=[NumberRange(0, 0), Optional()])
    knowledge_arcana = IntegerField(u'Knowledge Arcana', validators=[NumberRange(0, 0), Optional()])
    knowledge_dungeoneering = IntegerField(u'Knowledge - Dungeoneering', validators=[NumberRange(0, 0), Optional()])
    knowledge_engineering = IntegerField(u'Knowledge - Engineering', validators=[NumberRange(0, 0), Optional()])
    knowledge_geography = IntegerField(u'Knowledge - Geography', validators=[NumberRange(0, 0), Optional()])
    knowledge_history = IntegerField(u'Knowledge - History', validators=[NumberRange(0, 0), Optional()])
    knowledge_local = IntegerField(u'Knowledge - Local', validators=[NumberRange(0, 0), Optional()])
    knowledge_nature = IntegerField(u'Knowledge - Nature', validators=[NumberRange(0, 0), Optional()])
    knowledge_nobility = IntegerField(u'Knowledge - Nobility', validators=[NumberRange(0, 0), Optional()])
    knowledge_planes = IntegerField(u'Knowledge - Planes', validators=[NumberRange(0, 0), Optional()])
    knowledge_religion = IntegerField(u'Knowledge - Religion', validators=[NumberRange(0, 0), Optional()])
    linguistics = IntegerField(u'Linguistics', validators=[NumberRange(0, 0), Optional()])
    perception = IntegerField(u'Perception', validators=[NumberRange(0, 0), Optional()])
    perform_a = IntegerField(u'Perform A', validators=[NumberRange(0, 0), Optional()])
    perform_b = IntegerField(u'Perform B', validators=[NumberRange(0, 0), Optional()])
    profession_a = IntegerField(u'Profession A', validators=[NumberRange(0, 0), Optional()])
    profession_b = IntegerField(u'Profession B', validators=[NumberRange(0, 0), Optional()])
    ride = IntegerField(u'Ride', validators=[NumberRange(0, 0), Optional()])
    sense_motive = IntegerField(u'Sense Motive', validators=[NumberRange(0, 0), Optional()])
    sleight_of_hand = IntegerField(u'Sleight of Hand', validators=[NumberRange(0, 0), Optional()])
    spellcraft = IntegerField(u'Spellcraft', validators=[NumberRange(0, 0), Optional()])
    stealth = IntegerField(u'Stealth', validators=[NumberRange(0, 0), Optional()])
    survival = IntegerField(u'Survival', validators=[NumberRange(0, 0), Optional()])
    swim = IntegerField(u'Swim', validators=[NumberRange(0, 0), Optional()])
    use_magic_device = IntegerField(u'Use Magic Device', validators=[NumberRange(0, 0), Optional()])



class WTF_Weapon(Form):

    name = StringField(u'Name')
    attack_bonus = IntegerField(u'Attack Bonus', validators=[NumberRange(0, 0), Optional()])
    critical = IntegerField(u'Critical', validators=[NumberRange(0, 0), Optional()])
    dmg_type = IntegerField(u'Damage Type', validators=[NumberRange(0, 0), Optional()])
    wpn_range = IntegerField(u'Weapon Range', validators=[NumberRange(0, 0), Optional()])
    ammunition = IntegerField(u'Ammunition', validators=[NumberRange(0, 0), Optional()])
    damage = StringField(u'Damage')



class WTF_Armor(Form):

    name = StringField(u'Name')
    bonus = IntegerField(u'Bonus', validators=[NumberRange(0, 0), Optional()])
    armor_type = StringField(u'Armor Type', validators=[NumberRange(0, 0), Optional()])
    check_penalty = IntegerField(u'Check Penalty', validators=[NumberRange(0, 0), Optional()])
    spell_failure = IntegerField(u'Spell Failure', validators=[NumberRange(0, 0), Optional()])
    weight = IntegerField(u'Weight', validators=[NumberRange(0, 0), Optional()])
    properties = StringField(u'Properties')



class WTF_Item(Form):

    item = StringField(u'Item')
    weight = IntegerField(u'Weight', validators=[NumberRange(0, 0), Optional()])


class WTF_Charsheet(Form):
    attributes = FormField(WTF_Attributes)
    abilities = FormField(WTF_Abilities)
    skills = FormField(WTF_Skills)
    weapon = FormField(WTF_Weapon)
    armor = FormField(WTF_Armor)
    item = FormField(WTF_Item)
    submit = SubmitField()
