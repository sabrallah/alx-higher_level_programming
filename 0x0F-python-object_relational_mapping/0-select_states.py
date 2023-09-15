#!/usr/bin/python3
"""
Script listing all states from the hbtn_0e_0_usa database
"""

import sys
import MySQLdb


def main():
    """Main function"""

    # Connect to database
    connection = connect_to_db()

    # Get cursor
    cursor = connection.cursor()

    # Select query
    cursor.execute('SELECT * FROM states ORDER BY id ASC;')

    # Fetch results
    states = cursor.fetchall()

    # Print states
    print_states(states)

    # Close connection
    connection.close()


def connect_to_db():
    """Connect to database"""
    return MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306,
        host='localhost'
    )


def print_states(states):
    """Print states"""
    for state in states:
        print(state)


if __name__ == '__main__':
    main()
