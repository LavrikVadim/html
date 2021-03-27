from flask import Flask, render_template
from markupsafe import escape

import sqlite3


app = Flask(__name__)


@app.route('/')
def homepage():
    con = sqlite3.connect('articles.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM articles")
    con.commit()
    con.close()

    return render_template('mainpage.html')



@app.route('/about')
def hello_world1():
    return render_template('legendary car.html')

@app.route('/tech')
def hello_world2():
    return render_template('technologies.html')

@app.route('/new')
def hello_world3():
    return render_template('newitems.html')

@app.route('/about/<username>')
def about(username):
    return f'All about {escape(username)}'


if __name__ == '__main__':
    app.run()



