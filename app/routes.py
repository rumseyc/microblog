from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
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
