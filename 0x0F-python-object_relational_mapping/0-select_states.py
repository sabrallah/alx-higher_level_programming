#!/usr/bin/python3
"""
Thes scriptt list all state from the
databases `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accesse to tha databases and gets tha state
    from the database.
    """
    id = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                          passwd=argv[2], id=argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)
