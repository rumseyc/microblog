from app import app

@app.route('/')
@app.route('/index')
@app.route('/test')

def index():
    return "Hello World!"