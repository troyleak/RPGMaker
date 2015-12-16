#! /usr/bin/python

from flask import Flask, render_template, request

import secrets

from character import *
from forms import *

app = Flask(__name__)
app.secret_key = secrets.SECRET_KEY

@app.route("/")
def entry():
    return render_template("index.html")


@app.route("/form")
def form():
    skills = Skills(app)
    player = Character(skills) # create new character object to pass around and build

    attrib_form = WTF_Attributes()
    ability_form = WTF_Abilities()
    skills_form = WTF_Skills()
    items_form = WTF_Item()
    weapons_form = WTF_Weapon()
    armor_form = WTF_Armor()

    if (attrib_form.validate_on_submit()
        and ability_form.validate_on_submit()
        and skills_form.validate_on_submit() ):
        return redirect('/submit')


    return render_template('pathfinder.html',
                            attrib_form=attrib_form,
                            ability_form=ability_form,
                            skills_form=skills_form,
                            items_form=items_form,
                            weapons_form=weapons_form,
                            armor_form=armor_form)

@app.route("/submit", methods=('GET', 'POST'))
def submit():
    return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True)
