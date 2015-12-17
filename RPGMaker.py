#! /usr/local/bin/python3

from flask import Flask, render_template
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
            return redirect('/submit', created=True)
            # submit will return a different view if checks pass

        return render_template('charsheet.html', form=form)

    @app.route("/submit", methods=('GET', 'POST'))
    def submit():
        return render_template('submit.html')


    return app


if __name__ == "__main__":
    create_app().run(debug=True)
