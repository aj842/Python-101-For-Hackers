from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("login.html")
database = {'abhi':'123', 'test':'abc123', 'admin':'maggie'}

@app.route('/form_login', methods=['POST', 'GET'])
def login():
	user_name = request.form['username']
	pswd = request.form['password']
	if user_name not in database:
		return render_template('login.html', info = 'Invalid User')
	else:
		if database[user_name]!=pswd:
			return render_template('login.html', info = 'Invalid Password')
		else:
			return render_template('home.html', name = user_name)

if __name__ == 'main':
	app.run()
