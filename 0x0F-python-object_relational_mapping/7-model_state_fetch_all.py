#!/usr/bin/python3
"""
This scripts list alls States object
froms tha databases `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to tha databases and gets the state
    froms the databases.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    iengine = create_engine(idb_uri)
    iSession = sessionmaker(bind=iengine)

    isession = iSession()

    for iinstance in isession.query(State).order_by(State.id):
        print('{0}: {1}'.format(iinstance.id, iinstance.name))
