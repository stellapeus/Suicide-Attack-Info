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
    with open('suicide_attacks.json') as suicide_attacks:
        attacks = json.load(suicide_attacks)
    if "location" in request.args:
        number = 0
        for a in attacks:
            if a["target"]["country"] == request.args["location"]:
                number += 1
                
        return render_template("locationresponse.html", locations = location_options, num = number, country =  request.args["location"])
    return render_template("location.html", locations = location_options)
    
    
@app.route('/attacker')
def attacker():
    return render_template("attacker.html")
    
@app.route('/time')
def time():
    plot = get_suicide_points()
    return render_template("time.html", thePlot=plot)
    
    
def get_location_options():
    with open("suicide_attacks.json") as attacks:
        attacksData = json.load(attacks)
    locations = []
    for attack in attacksData:
        if attack["target"]["country"] not in locations:
            locations.append(attack["target"]["country"])
    return locations
    
def get_suicide_points():
    with open("suicide_attacks.json") as attacks:
        attacksData = json.load(attacks)
    time={}
    for t in time:
        time[str(t['year']) == t['wounded_low']]
    print(time)
    plot_suicide_points =""
    for key, value in time.items():
        plot_suicide_points = plot_suicide_points + Markup({x: ' + str(key) + ', y: '+ str(value) +'})
    return plot_suicide_points    
    
    
if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production
    
    
    
 