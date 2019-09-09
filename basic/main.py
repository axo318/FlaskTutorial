from flask import Flask, render_template, redirect, url_for, request

# Vars
PORT = 5000
HOST = '0.0.0.0'

# Start serving
app = Flask(__name__)


# Home page
'''
Here we have to return the html page called 'index.html' using the method 'render_template'
This serves the html page whenever the user visits the default url of the website
'''
@app.route('/')
@app.route('/index')
def index():
	pass


# Login page
'''
Here we have to return the html page called 'login.html' using the method 'render_template'
'''
@app.route('/login')
def login():
	pass


# Authentication page
'''
Here we have to retrieve the username and password that the user has submitted from the login page and check them
If they are right, we have to serve the page 'home.html' to the user, passing the username as a parameter in render_template
If they are wrong, we have to redirect the user back to login, using the redirect(url_for()) method with 'login' as parameter

'''
@app.route('/auth')
def auth():
	pass


# MAIN method
if __name__=='__main__':
	app.run(host=HOST, port=PORT)