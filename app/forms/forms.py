# from flask_wtf import Form
from wtforms import validators
from wtforms import Form, StringField as strf, IntegerField as intf, FormField, SubmitField

# TODO: Finish validate input
#       Plug frontend into backend

# Originally intended to use flask_wtf for this, however due to a bug in
# CSRF token handling with nested formfields, I'm using the default wtform lib

class WTF_Attributes(Form):
    name = strf(u'Name', validators=[validators.Required()])
    level = intf(u'Level', validators=[validators.Required(), validators.NumberRange(0, 0)])
    player = strf(u'Player', validators=[validators.Required()])
    gender = strf(u'Gender', validators=[validators.Required()])
    race = strf(u'Race', validators=[validators.Required()])
    size = strf(u'Size', validators=[validators.Required()])
    age = strf(u'Age', validators=[validators.Required()])
    height = intf(u'Height', validators=[validators.Required(), validators.NumberRange(0, 0)])
    weight = intf(u'Weight', validators=[validators.Required(), validators.NumberRange(0, 0)])
    hair = strf(u'Hair', validators=[validators.Required()])
    eyes = strf(u'Eyes', validators=[validators.Required()])
    alignment = strf(u'Alignment', validators=[validators.Required()])
    deity = strf(u'Deity', validators=[validators.Required()])
    homeland = strf(u'Homeland', validators=[validators.Required()])



class WTF_Abilities(Form):

    strength = intf(u'Strength', validators=[validators.Required(), validators.NumberRange(0, 0)])
    dexterity = intf(u'Dexterity', validators=[validators.Required(), validators.NumberRange(0, 0)])
    constitution = intf(u'Constitution', validators=[validators.Required(), validators.NumberRange(0, 0)])
    intelligence = intf(u'Intelligence', validators=[validators.Required(), validators.NumberRange(0, 0)])
    wisdom = intf(u'Wisdom', validators=[validators.Required(), validators.NumberRange(0, 0)])
    charisma = intf(u'Charisma', validators=[validators.Required(), validators.NumberRange(0, 0)])



class WTF_Skills(Form):

    acrobatics = intf(u'Acrobatics', validators=[validators.Required(), validators.NumberRange(0, 0)])
    appraise = intf(u'Appraise', validators=[validators.Required(), validators.NumberRange(0, 0)])
    bluff = intf(u'Bluff', validators=[validators.Required(), validators.NumberRange(0, 0)])
    climb = intf(u'Climb', validators=[validators.Required(), validators.NumberRange(0, 0)])
    craft_a = intf(u'Craft a', validators=[validators.Required(), validators.NumberRange(0, 0)])
    craft_b = intf(u'Craft b', validators=[validators.Required(), validators.NumberRange(0, 0)])
    craft_c = intf(u'Craft c', validators=[validators.Required(), validators.NumberRange(0, 0)])
    diplomacy = intf(u'Diplomacy', validators=[validators.Required(), validators.NumberRange(0, 0)])
    disable_device = intf(u'Disable Device', validators=[validators.Required(), validators.NumberRange(0, 0)])
    disguise = intf(u'Disguise', validators=[validators.Required(), validators.NumberRange(0, 0)])
    escape_artist = intf(u'Escape Artist', validators=[validators.Required(), validators.NumberRange(0, 0)])
    fly = intf(u'Fly', validators=[validators.Required(), validators.NumberRange(0, 0)])
    handle_animal = intf(u'Handle Animal', validators=[validators.Required(), validators.NumberRange(0, 0)])
    heal = intf(u'Heal', validators=[validators.Required(), validators.NumberRange(0, 0)])
    intimidate = intf(u'Intimidate', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_arcana = intf(u'Knowledge Arcana', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_dungeoneering = intf(u'Knowledge - Dungeoneering', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_engineering = intf(u'Knowledge - Engineering', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_geography = intf(u'Knowledge - Geography', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_history = intf(u'Knowledge - History', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_local = intf(u'Knowledge - Local', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_nature = intf(u'Knowledge - Nature', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_nobility = intf(u'Knowledge - Nobility', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_planes = intf(u'Knowledge - Planes', validators=[validators.Required(), validators.NumberRange(0, 0)])
    knowledge_religion = intf(u'Knowledge - Religion', validators=[validators.Required(), validators.NumberRange(0, 0)])
    linguistics = intf(u'Linguistics', validators=[validators.Required(), validators.NumberRange(0, 0)])
    perception = intf(u'Perception', validators=[validators.Required(), validators.NumberRange(0, 0)])
    perform_a = intf(u'Perform A', validators=[validators.Required(), validators.NumberRange(0, 0)])
    perform_b = intf(u'Perform B', validators=[validators.Required(), validators.NumberRange(0, 0)])
    profession_a = intf(u'Profession A', validators=[validators.Required(), validators.NumberRange(0, 0)])
    profession_b = intf(u'Profession B', validators=[validators.Required(), validators.NumberRange(0, 0)])
    ride = intf(u'Ride', validators=[validators.Required(), validators.NumberRange(0, 0)])
    sense_motive = intf(u'Sense Motive', validators=[validators.Required(), validators.NumberRange(0, 0)])
    sleight_of_hand = intf(u'Sleight of Hand', validators=[validators.Required(), validators.NumberRange(0, 0)])
    spellcraft = intf(u'Spellcraft', validators=[validators.Required(), validators.NumberRange(0, 0)])
    stealth = intf(u'Stealth', validators=[validators.Required(), validators.NumberRange(0, 0)])
    survival = intf(u'Survival', validators=[validators.Required(), validators.NumberRange(0, 0)])
    swim = intf(u'Swim', validators=[validators.Required(), validators.NumberRange(0, 0)])
    use_magic_device = intf(u'Use Magic Device', validators=[validators.Required(), validators.NumberRange(0, 0)])



class WTF_Weapon(Form):

    name = strf(u'Name', validators=[validators.Required()])
    attack_bonus = intf(u'Attack Bonus', validators=[validators.Required(), validators.NumberRange(0, 0)])
    critical = intf(u'Critical', validators=[validators.Required(), validators.NumberRange(0, 0)])
    dmg_type = intf(u'Damage Type', validators=[validators.Required(), validators.NumberRange(0, 0)])
    wpn_range = intf(u'Weapon Range', validators=[validators.Required(), validators.NumberRange(0, 0)])
    ammunition = intf(u'Ammunition', validators=[validators.Required(), validators.NumberRange(0, 0)])
    damage = strf(u'Damage', validators=[validators.Required()])



class WTF_Armor(Form):

    name = strf(u'Name', validators=[validators.Required()])
    bonus = intf(u'Bonus', validators=[validators.Required(), validators.NumberRange(0, 0)])
    armor_type = strf(u'Armor Type', validators=[validators.Required(), validators.NumberRange(0, 0)])
    check_penalty = intf(u'Check Penalty', validators=[validators.Required(), validators.NumberRange(0, 0)])
    spell_failure = intf(u'Spell Failure', validators=[validators.Required(), validators.NumberRange(0, 0)])
    weight = intf(u'Weight', validators=[validators.Required(), validators.NumberRange(0, 0)])
    properties = strf(u'Properties', validators=[validators.Required()])



class WTF_Item(Form):

    item = strf(u'Item', validators=[validators.Required()])
    weight = intf(u'Weight', validators=[validators.Required(), validators.NumberRange(0, 0)])


class WTF_Charsheet(Form):
    attributes = FormField(WTF_Attributes)
    abilities = FormField(WTF_Abilities)
    skills = FormField(WTF_Skills)
    weapon = FormField(WTF_Weapon)
    armor = FormField(WTF_Armor)
    item = FormField(WTF_Item)
    submit = SubmitField('Submit')
