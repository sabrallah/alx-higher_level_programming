#!/usr/bin/python3
"""
This scripts  takes in the names of a states
as an arguments and list all cities of thats
states, using the databases `hbtn_0e_4_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to tha databases and gets the citie
    froms the databases.
    """

    idb = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                          passwd=argv[2], idb=argv[3])

    with idb.cursor() as icur:
        icur.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': argv[4]
        })

        irows = icur.fetchall()

    if irows is not None:
        print(", ".join([row[1] for row in irows]))
