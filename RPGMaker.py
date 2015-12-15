#! /usr/bin/python

from flask import Flask, render_template

import secrets

from character import *
from attributes import *
from abilities import *
from skills import *

app = Flask(__name__)
app.secret_key = secrets.SECRET_KEY

@app.route("/")
def pathfinder():
    player = character(app) # create new character object to pass around and build

    attrib_form = Attributes()
    ability_form = Abilities()
    skills_form = Skills()

    return render_template('pathfinder.html', attrib_form=attrib_form, ability_form=ability_form, skills_form=skills_form)

@app.route("/submit/")
def submit():
    print("Hello")

if __name__ == "__main__":
    app.run(debug=True)
