from flask import Flask, render_template
app = Flask(__name__)

import json
from flask import jsonify

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/todaysprice')
def getTodaysPrice():
    return render_template('todays_price.html')

@app.route('/api/todaysprice')
def getTodaysPriceAPI():
    with open('dumps/todaysprice.json')as f:
        data=f.read()
    return jsonify(json.loads(data))