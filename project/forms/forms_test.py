from flask_wtf import Form
from wtforms import validators
from wtforms import StringField, IntegerField, FormField, SubmitField

# TODO: Finish validate input
#       Plug frontend into backend

class WTF_Attributes(Form):
    name = StringField(u'Name', [validators.DataRequired() ])
    level = IntegerField(u'Level', [validators.DataRequired(), validators.NumberRange(min=0, max=20) ])

class WTF_Abilities(Form):
    strength = IntegerField(u'Strength', [validators.DataRequired(), validators.NumberRange(min=0, max=20) ])

class WTF_Charsheet(Form):
    attributes = FormField(WTF_Attributes)
    abilities = FormField(WTF_Abilities)
    submit = SubmitField('Submit')
