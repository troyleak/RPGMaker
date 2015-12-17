#! /usr/local/bin/python3
'''
RPGMaker

Creates a character sheet for Pathfinder RPG

User can put in as much information as they want. Values not submitted will be
randomized. After randomization, returns character for review.

User can modify character sheet as many times as they need.

At the end the character sheet can be printed to PDF (or other file)



Main program:

    Creates character and passes it around. The end result will be
    a tree-like structure containing at the highest level only information about
    basic attributes like class, race, etc. The attribute classes will contain
    information about and application logic for the options of that attribute


    I realize this is large in scope, most of the logic should already be
    implemented though

    TODO:   Need to tie frontend and backend together. Most of the hard work should
                already be done. Just have to have form submission update character
                model based on validation results

            Error catching - can be done in the individual classes

            Fix frontend glitches - (low priority)

'''

from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap

import secrets

from character import *
from forms import *

def create_app(configfile=None):
    app = Flask(__name__)
    Bootstrap(app)
    app.secret_key = secrets.SECRET_KEY

    @app.route("/")
    def entry():
        return render_template("index.html")


    @app.route("/form")
    def form():
        char_skills = Skills(app)
        player = Character(app) # create new character object to pass around and build

        form = WTF_Charsheet()

        if (form.validate_on_submit()):
            return redirect(url_for(submit), created=True)

        return render_template('charsheet.html', form=form)

    @app.route("/submit", methods=('GET', 'POST'))
    def submit():
        return render_template('submit.html', created=created)


    return app


if __name__ == "__main__":
    create_app().run(debug=True)
