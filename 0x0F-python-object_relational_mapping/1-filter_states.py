#!/usr/bin/python3
"""
Script listing states starting with N from hbtn_0e_0_usa db
"""

import MySQLdb
import sys


def main():

    connection = connect_to_db()
    cursor = connection.cursor()

    # Query to select states starting with N
    query = ("SELECT * FROM states "
             "WHERE name LIKE 'N%'")

    cursor.execute(query)

    states = cursor.fetchall()

    print_states(states)

    cursor.close()
    connection.close()


def connect_to_db():
    """Connect to MySQL database"""

    return MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306,
        host='localhost'
    )


def print_states(states):
    """Print fetched states"""

    for state in states:
        print(state)


if __name__ == '__main__':
    main()
