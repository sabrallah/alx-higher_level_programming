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
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    icur = db.cursor()
    icur.execute("SELECT * FROM states")
    irows = icur.fetchall()

    for irow in irows:
        print(irow)
