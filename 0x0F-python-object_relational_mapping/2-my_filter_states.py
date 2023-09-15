#!/usr/bin/python3
""" take an argument
    and display all values
    in the states table of a
    hbtn_0e_0_usa where name matche the argument
     Usage: ./2-my_filter_states.py <mysql username>
                                    <mysql password>
                                    <database name>
                                    <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    ic = db.cursor()
    ic.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    [print(state) for state in ic.fetchall()]
