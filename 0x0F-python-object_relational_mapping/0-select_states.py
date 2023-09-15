#!/usr/bin/python3
"""
This scripts lists alls state froms the
databases `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access tos tha databases and gets the state
    froms the database.
    """
    idb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], idb=argv[3])

    cur = idb.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
