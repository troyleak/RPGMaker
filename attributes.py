from flask_wtf import Form
from wtforms import validators, StringField

class Attributes(Form):
    name = StringField(u'name', validators=[validators.input_required()])
    level = StringField(u'level', validators=[validators.input_required()])
    player = StringField(u'player', validators=[validators.input_required()])
    gender = StringField(u'gender', validators=[validators.input_required()])
    race = StringField(u'race', validators=[validators.input_required()])
    size = StringField(u'size', validators=[validators.input_required()])
    age = StringField(u'age', validators=[validators.input_required()])
    height = StringField(u'height', validators=[validators.input_required()])
    weight = StringField(u'weight', validators=[validators.input_required()])
    hair = StringField(u'hair', validators=[validators.input_required()])
    eyes = StringField(u'eyes', validators=[validators.input_required()])
    alignment = StringField(u'alignment', validators=[validators.input_required()])
    deity = StringField(u'deity', validators=[validators.input_required()])
    homeland = StringField(u'homeland', validators=[validators.input_required()])
