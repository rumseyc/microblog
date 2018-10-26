"""
high level support for doing this and that.
"""
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    """hi support for doing this and that."""
    user = {'username': 'Carl Rumsey'}
    posts = [
        {
            'author': {'username': 'Jordi'},
            'body': 'Euchre is too easy!'
        },
        {
            'author': {'username': 'Pepe'},
            'body': 'Im never playing with you again!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """hi support for doing this and that."""
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
