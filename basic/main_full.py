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
	return render_template('index.html')
	
# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html', msg='')

# Authentication page
@app.route('/auth', methods=['GET', 'POST'])
def auth():
	user = request.form.get('user')
	password = request.form.get('pass')
	if user =='user' and password =='pass':
		return render_template('home.html', user=user)
	else:
		return redirect(url_for('login', msg='failed login attempt'))


# MAIN method
if __name__=='__main__':
	app.run(host=HOST, port=PORT)