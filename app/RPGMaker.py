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
    a tree-like structure containing at the highest level only an interface for
    basic attributes like class, race, etc. The attribute classes will contain
    information about and application logic for the options of that attribute


    I realize this is large in scope, most of the logic should already be
    implemented though

    TODO:   Need to tie frontend and backend together. Most of the hard work should
                already be done. Just have to have form submission update character
                model based on validation results

            Error catching - can be done in the individual classes

            Fix frontend glitches - Want form data accepted and displayed

            Fix packaging. Figure out class structure

'''

from flask import Flask, render_template, flash, redirect, url_for, session, request
from flask_bootstrap import Bootstrap

from character_gen import *
from secrets import *

from forms import *


app = Flask(__name__)
app.secret_key = '\xda\xd2\x02\xa1w\xd3B\x93\x93\x8e"\xc0n\x14\xc4w\xc4\x10\xf2\xba\t\x8b0\xb9'
# app.config.from_object('secrets')

Bootstrap(app)

char = character.Character()


@app.route("/")
def entry():
    return render_template("index.html")


@app.route("/form", methods=('GET', 'POST'))
def form():

    form = forms.WTF_Charsheet()
    session['submitted_form'] = form.data

    if request.method == 'POST' and form.validate():
        app.logger.debug(form.data)
        return redirect(url_for('submit'))

    # app.logger.debug(form.errors)
    return render_template('charsheet.html', form=form, char=char)


@app.route("/submit", methods=('GET', 'POST'))
def submit():
    form_data = session['submitted_form']
    return render_template('submit.html', form=form, char=char, form_data=form_data)



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
