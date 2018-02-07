from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    users = {'username' : 'habibi'}
    posts = [
                {
                    'author' : {'username' : 'John'},
                    'body' : 'Test post by john'
                },
                {
                    'author' : {'username' : 'Mary'},
                    'body' : 'The avngers movie'
                }
            ]
    return render_template('index.html', title='Home', user=users, posts=posts)

