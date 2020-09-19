from flask import Flask, render_template, jsonify
import os
import json

from shares import NepseScrapper

app = Flask(__name__)
HOST = 'localhost'
PORT = 5000

@app.route('/')
def welcome():
    if not os.path.isfile('dumps/todayshare.json') or \
    not os.path.isfile('template/todays_share.html'):
        obj = NepseScrapper()
        obj.fetch_all_datas()
    return render_template('index.html')

@app.route('/todaysprice')
def getTodaysPrice():
    return render_template('todays_share.html')

@app.route('/api/todaysprice')
def getTodaysPriceAPI():
    with open('dumps/todayshare.json')as f:
        data=f.read()
    return jsonify(json.loads(data))

@app.route('/gainers')
def getGainers():
    return render_template('gainers.html')

@app.route('/api/gainers')
def getGainersAPI():
    with open('dumps/gainers.json')as f:
        data=f.read()
    return jsonify(json.loads(data))

@app.route('/losers')
def getLosers():
    return render_template('losers.html')

@app.route('/api/losers')
def getLosersAPI():
    with open('dumps/losers.json')as f:
        data=f.read()
    return jsonify(json.loads(data))

if __name__ == '__main__':
    app.debug = True
    app.run(host=HOST, port=PORT, threaded=False)