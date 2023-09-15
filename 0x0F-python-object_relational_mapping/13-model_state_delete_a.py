#!/usr/bin/python3

import mysql.connector
from model_state import Base, State

def delete_states_with_a(username, password, database):
    """
    Delete all State objects with a name containing the letter a from the database.
    """
    conn = mysql.connector.connect(
        user=username,
        password=password,
        host='localhost',
        database=database
    )
    cursor = conn.cursor()

    query = "DELETE FROM State WHERE name LIKE '%a%'"

    cursor.execute(query)

    conn.commit()

    cursor.close()
    conn.close()
