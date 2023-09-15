#!/usr/bin/python3

import MySQLdb
import sys

def connect():
    return MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost', 
        port=3306
    )

def get_states():
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')
    states = cursor.fetchall()
    
    conn.close()
    return states

def print_states(states):
    for state in states:
        print(state)

if __name__ == '__main__':
    states = get_states()
    print_states(states)
