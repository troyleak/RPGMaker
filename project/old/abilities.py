from flask_wtf import Form
from wtforms import validators, StringField

class Abilities(Form):

    strength = StringField(u'Strength', validators=[validators.input_required()])
    dexterity = StringField(u'Dexterity', validators=[validators.input_required()])
    constitution = StringField(u'Constitution', validators=[validators.input_required()])
    intelligence = StringField(u'Intelligence', validators=[validators.input_required()])
    wisdom = StringField(u'Wisdom', validators=[validators.input_required()])
    charisma = StringField(u'Charisma', validators=[validators.input_required()])

    def get_values(strength, dexterity, constitution, intelligence, wisdom, charisma):
        return abilities
