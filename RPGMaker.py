#! /usr/bin/python

from flask import Flask, render_template
from character import *

app = Flask(__name__)

@app.route("/")
def pathfinder():
    player = character(app) # create new character object to pass around and build
    print(player)
    return render_template('pathfinder.html')

if __name__ == "__main__":
    app.run(debug=True)
