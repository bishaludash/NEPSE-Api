from flask import Flask, render_template, jsonify
import json

import os
import shares

app = Flask(__name__)
HOST = 'localhost'
PORT = 5000

@app.route('/')
def welcome():
    if not os.path.isfile('dumps/todaysprice.json') or \
    not os.path.isfile('template/todays_price.html'):
        shares.fetch_todays_share()
    return render_template('index.html')

@app.route('/todaysprice')
def getTodaysPrice():
    return render_template('todays_price.html')

@app.route('/api/todaysprice')
def getTodaysPriceAPI():
    with open('dumps/todayshare.json')as f:
        data=f.read()
    return jsonify(json.loads(data))


if __name__ == '__main__':
    app.debug = True
    app.run(host=HOST, port=PORT, threaded=False)