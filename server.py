from flask import Flask, url_for
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')







app.run(host='localhost', port=3033, debug=True)
