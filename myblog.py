from flask import Flask, render_template, url_for, flash, redirect
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

@app.route("/register", methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password!', 'danger')
	return render_template('login.html', title='Login', form=form)



if __name__ == "__main__":
	app.run(debug = True)
