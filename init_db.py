#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('hockey.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO players (fname, lname, position, rank) VALUES (?, ?, ?, ?)",
            ('leila', 'kemery', 'defense', 3)
            )

cur.execute("INSERT INTO players (fname, lname, position, rank) VALUES (?, ?, ?, ?)",
            ('dale', 'kemery', 'defense', 1)
            )

connection.commit()
connection.close()
