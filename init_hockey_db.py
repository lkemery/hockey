#!/usr/bin/python3
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    cur = conn.cursor() 
    cur.execute('SELECT * FROM users')
    result = cur.fetchall()
    print(result)
    cur.close()
    conn.close()

def main():
   
    database = r"hockey.db"

    # create a database connection
    conn = None
     
    with open('nw_schema_hockey.sql', 'r') as sql_file:
        sql = sql_file.read()

    conn = create_connection(database)
    print('database connected..')
   
    

if __name__ == "__main__":
    main()
    


