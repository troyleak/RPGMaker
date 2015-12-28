# from flask_wtf import Form
from wtforms.validators import *
from wtforms import Form, StringField, IntegerField, FormField, SubmitField, validators

# TODO: Debug validate input - Required input works, but numberrange doesn't
#       Plug frontend into backend

class WTF_Attributes(Form):
    name = StringField(u'Name', validators=[ InputRequired(), Required() ])
    level = IntegerField(u'Level', validators=[ NumberRange(min=1, max=20), InputRequired(), Required()])

class WTF_Abilities(Form):
    strength = IntegerField(u'Strength', validators=[ InputRequired(), NumberRange(min=1, max=20), Required() ])

class WTF_Skills(Form):
    acrobatics = IntegerField(u'Acrobatics', validators=[validators.Required(), validators.NumberRange(0, 0)])

class WTF_Weapon(Form):
    name = StringField(u'Name', validators=[validators.Required()])

class WTF_Armor(Form):
    name = StringField(u'Name', validators=[validators.Required()])

class WTF_Item(Form):
    item = StringField(u'Item', validators=[validators.Required()])

class WTF_Charsheet(Form):
    attributes = FormField(WTF_Attributes)
    abilities = FormField(WTF_Abilities)
    skills = FormField(WTF_Skills)
    weapon = FormField(WTF_Weapon)
    armor = FormField(WTF_Armor)
    item = FormField(WTF_Item)
    submit = SubmitField('Submit')
