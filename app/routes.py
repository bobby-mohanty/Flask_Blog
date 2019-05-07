from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post
from app import app, db, bcrypt

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unseccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)