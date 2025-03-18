from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
]

quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fun', methods=['GET'])
def fun():
    return jsonify({"joke": random.choice(jokes)})

@app.route('/quote', methods=['GET'])
def quote():
    return jsonify({"quote": random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
