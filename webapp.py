from flask import Flask, request, render_template, flash
from markupsafe import Markup

import os
import json

app = Flask(__name__)     

@app.route('/')
def home():
    return render_template("data.html")
    
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/location')
def location():
    location_options = get_location_options()
    return render_template("location.html", locations = location_options)
    
@app.route('/attacker')
def attacker():
    return render_template("attacker.html")
    
@app.route('/time')
def time():
    return render_template("time.html")
    
def get_location_options():
    with open("suicide_attacks.json") as attacks:
        attacksData = json.load(attacks)
    locations = []
    for attack in attacksData:
        if attack["target"]["country"] not in locations:
            locations.append(attack["target"]["country"])
    return locations
    
if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production
    
 