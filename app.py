from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)
HOST = 'localhost'
PORT = 5000

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


if __name__ == '__main__':
    app.debug = True
    app.run(host=HOST, port=PORT, threaded=False)