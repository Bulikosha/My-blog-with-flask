from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "2bdeb612567270f4a9082a62346ef5b0"
"""We can generate secret key with Python by running Python interpreter and type:
		import secrets
		secrets.token_hex(16)
Then copy generated string"""

posts = [
	{
		'title': 'My Post 1',
		'content': 'Content for the post 1',
		'date_posted': '30 April 2020'
	},
	{
		'title': 'My Post 2',
		'content': 'Content for the post 2',
		'date_posted': '14 May 2020'
	}

]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)



if __name__ == "__main__":
	app.run(debug = True)
