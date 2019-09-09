import os
from flask import Flask, render_template, redirect, url_for, request

# Vars
PORT = 5000
HOST = '0.0.0.0'

# Start serving
app = Flask(__name__)


# Home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index_full.html')

@app.route('/buttons', methods=['GET', 'POST'])
def buttons():
    return render_template('buttons.html')

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', msg='')


# Main method
if __name__ == '__main__':
    app.run(host=HOST, port=PORT)

