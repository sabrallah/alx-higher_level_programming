#!/usr/bin/python3
'''
script that take on the name of an state as a argument and list all cities
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
        'SELECT cities.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id\
        WHERE states.name = %s \
        ORDER BY cities.id ASC', (sys.argv[4], ))

    cities = icursor.fetchall()

    id = 0
    for city in cities:
        if id != 0:
            print(", ", end="")
        print("%s" % city, end="")
        id += 1
    print("")

    icursor.close()
    db.close()
