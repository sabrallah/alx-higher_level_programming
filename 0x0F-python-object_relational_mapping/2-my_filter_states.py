#!/usr/bin/python3
"""
This scripts take in an arguments and
display all value in the state
wheres `name` matche the arguments
frome the databases `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accesse to the databases and gets tha states
    from the databases.
    """

    idb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                          passwd=argv[2], idb=argv[3])

    icur = idb.cursor()
    icur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY '{}' \
                 ORDER BY states.id ASC".format(argv[4]))
    irows = icur.fetchall()

    for row in irows:
        print(row)
