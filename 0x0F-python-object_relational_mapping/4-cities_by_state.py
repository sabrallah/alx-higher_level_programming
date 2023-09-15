#!/usr/bin/python3
'''
scripts that list  all the  cities from the a database
'''

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost')

    icursor = db.cursor()
    icursor.execute(
        'SELECT cities.id, cities.name, states.name FROM cities JOIN states ON\
        cities.state_id = states.id;')

    states = icursor.fetchall()

    for state in states:
        print(state)
