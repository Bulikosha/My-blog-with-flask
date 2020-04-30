from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html')




if __name__ == "__main__":
	app.run(debug = True)
