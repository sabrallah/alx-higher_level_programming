#!/usr/bi/python3
"""
Script listing states starting with N from 'hbtn_0e_0_usa' database
"""

import MySQLdb
import sys


def main():
    """Main function"""

    connection = connect_to_db()
    cursor = get_cursor(connection)

    # Query to select states starting with N
    query = ("SELECT * FROM states "
             "WHERE name LIKE 'N%'")

    execute_query(cursor, query)
    fetched_states = fetch_states(cursor)

    print_states(fetched_states)

    close_resources(cursor, connection)


def connect_to_db():
    """Connect to MySQL database"""
    return MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306,
        host='localhost')


def get_cursor(connection):
    return connection.cursor()


def execute_query(cursor, query):
    cursor.execute(query)


def fetch_states(cursor):
    return cursor.fetchall()


def print_states(states):
    for state in states:
        print(state)


def close_resources(cursor, connection):
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
