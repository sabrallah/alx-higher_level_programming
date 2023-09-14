#!/usr/bin/python3
"""
Thes scripts list all state with
a `name` starting with tha letters `N`
frome tha databases `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accesse to tha databases and gets the states
    froms tha databases.
    """
    idb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], idb=argv[3])

    icur = idb.cursor()
    icur.execute("SELECT * FROM states \
                 WHERE name LIKE BINARY 'N%' \
                 ORDER BY states.id ASC")
    irows = icur.fetchall()

    for row in irows:
        print(row)
