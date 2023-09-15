#!/usr/bin/python3
"""
This scripts change the names of an States object
from the databases `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Updates a States objects on the databases.
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
