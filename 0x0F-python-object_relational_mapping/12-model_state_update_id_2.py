#!/usr/bin/python3
"""
This script changes the name of a State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a State object on the database.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    iengine = create_engine(idb_uri)
    iSession = sessionmaker(bind=iengine)

    isession = iSession()

    iari_state = isession.query(State).filter(State.id == '2').first()
    iari_state.name = 'New Mexico'
    isession.commit()
    isession.close()
