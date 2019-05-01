from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Bobby',
        'title': 'Post 1',
        'content': 'First post content',
        'date_posted': 'April 30, 2019'
    },
    {
        'author': 'Meena',
        'title': 'Post 2',
        'content': 'Second post content',
        'date_posted': 'April 29, 2019'
    },
    {
        'author': 'Saroj',
        'title': 'Post 3',
        'content': 'Third post content',
        'date_posted': 'April 28, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == "__main__":
    app.run(debug=True)