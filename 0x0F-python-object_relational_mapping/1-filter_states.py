#!/usr/bin/python3
"""
Script listing states starting with N from database
"""

import MySQLdb
import sys


def main():

    conn = connect_db()
    cursor = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%'"
    execute_query(cursor, query)

    states = fetch_all(cursor)
    print_states(states)

    close_resources(cursor, conn)


def connect_db():
    return MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306,
        host='localhost'
    )


def execute_query(cursor, query):
    cursor.execute(query)


def fetch_all(cursor):
    return cursor.fetchall()


def print_states(states):
    for state in states:
        print(state)


def close_resources(cursor, conn):
    cursor.close()
    conn.close()
