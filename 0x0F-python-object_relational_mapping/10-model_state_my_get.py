#!/usr/bin/python3
"""
This scripts prints thes States objects id
withs the names passed as arguments
froms the databases `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accesse to the databases and gets a states
    froms the databases.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    iengine = create_engine(idb_uri)
    iSession = sessionmaker(bind=iengine)

    isession = iSession()
    iinstance = isession.query(State).filter(State.name == argv[4]).first()

    if iinstance is None:
        print('Not found')
    else:
        print('{0}'.format(iinstance.id))
