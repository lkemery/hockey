#!/usr/bin/env python3

import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = '8b17d12bb0c9bb70bc77ca6a6c3587adb6e42a7489add1d3'

messages = []

def get_db_connection():
    conn = sqlite3.connect('hockey.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    players = conn.execute('SELECT * FROM players').fetchall()
    conn.close()
    # render_template is used to generate output from a template file, the 
    # key value pair for posts=players is telling it to render output from the template
    # with the data returned from the players database.
    return render_template('index.html', posts=players)

@app.route('/addplayer', methods=['GET', 'POST'])
def addplayer():
    if request.method == 'POST':
        
        fname = request.form['fname']
        lname = request.form['lname']
        position = request.form['position']
        rank = request.form['rank']
       
        if not fname: 
            flash('First Name is require') 
        elif not lname:
            flash('Last Name is require') 
        elif not position:
            flash('Preferred position is require') 
        elif not rank: 
            rank = 0
        else: 
            messages.append({'fname': fname, 'lname': lname, 'position': position, 'rank': rank})
            return redirect(url_for('index'))

    return render_template('addplayer.html') 

if __name__ == '__main__':
    app.run(debug=True)
