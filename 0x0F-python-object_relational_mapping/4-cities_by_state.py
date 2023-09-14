#!/usr/bin/python3
"""
This scripts list all citie froms
tha databases `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Accesse to tha databases and gets the citie
    froms the databases.
    """

    idb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], idb=argv[3])

    with idb.cursor() as icur:
        icur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        irows = icur.fetchall()

    if irows is not None:
        for row in irows:
            print(row)
