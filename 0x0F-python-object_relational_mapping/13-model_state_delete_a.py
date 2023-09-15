#!/usr/bin/python3
"""
This scripts delete all States object
withs a names containing tha letters `a`
froms the databases `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Delete States object on tha database.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    iengine = create_engine(idb_uri)
    iSession = sessionmaker(bind=iengine)

    isession = iSession()

    for instance in isession.query(State).filter(State.name.contains('a')):
        isession.delete(instance)

    isession.commit()
    isession.close()
