#!/usr/bin/python3
import sqlite3
from sqlite3 import Error

print('starting..')
database = r"hockey.db"

# create a database connection
conn = None
     
try: 
    with open('nw_schema_hockey.sql', 'r') as sql_file:
        sql = sql_file.read()
    conn = sqlite3.connect(database)
    print('database connected..')
    curs = conn.cursor()
    print('executing sql file')
    curs.executescript(sql)
    print('committing')
    conn.commit()
    print('selecting from table users...')
    sql = 'Select * From users;'
    ply = 'Select * From players;'
    curs.execute(sql)
    curs.execute(ply)
    users = curs.fetchall()
    for user in users:
        print(user)
except Error as e: 
    print(e)
finally: 
    if conn:
        conn.close()
        print('done')
