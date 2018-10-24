from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
@app.route('/test')

def index():
    user = {'username': 'Carl Rumsey'}
    return render_template('index.html', title='Home', user=user)