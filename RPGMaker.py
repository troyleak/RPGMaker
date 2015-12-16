#! /usr/local/bin/python3

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import secrets

from character import *
from forms import *

def create_app(configfile=None):
    app = Flask(__name__)
    # app = Bootstrap(app)
    app.secret_key = secrets.SECRET_KEY

    @app.route("/")
    def entry():
        return render_template("index.html")


    @app.route("/form")
    def form():
        char_skills = Skills(app)
        player = Character(app) # create new character object to pass around and build

        attrib_form = WTF_Attributes()
        ability_form = WTF_Abilities()
        skills_form = WTF_Skills()
        items_form = WTF_Item()
        weapons_form = WTF_Weapon()
        armor_form = WTF_Armor()

        print(attrib_form.errors)

        if (attrib_form.validate_on_submit()
            and ability_form.validate_on_submit()
            and skills_form.validate_on_submit()
            and items_form.validate_on_submit()
            and weapons_form.validate_on_submit()
            and armor_form.validate_on_submit() ):
            return redirect('/submit', created=True)
            # submit will return a different view if checks pass

        print(attrib_form.errors)

        return render_template('charsheet.html',
                                attrib_form=attrib_form,
                                ability_form=ability_form,
                                skills_form=skills_form,
                                items_form=items_form,
                                weapons_form=weapons_form,
                                armor_form=armor_form)

    @app.route("/submit", methods=('GET', 'POST'))
    def submit():
        return render_template('submit.html')


    return app


if __name__ == "__main__":
    create_app().run(debug=True)
