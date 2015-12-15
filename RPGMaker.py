#! /usr/bin/python

from flask import Flask, render_template

from character import *
from attributes import *
from abilities import *
from skills import *

app = Flask(__name__)

@app.route("/")
def pathfinder():
    player = character(app) # create new character object to pass around and build

    attrib_form = Attributes(csrf_enabled=False)
    ability_form = Abilities(csrf_enabled=False)
    skills_form = Skills(csrf_enabled=False)

    return render_template('pathfinder.html', attrib_form=attrib_form, ability_form=ability_form, skills_form=skills_form)

if __name__ == "__main__":
    app.run(debug=True)
