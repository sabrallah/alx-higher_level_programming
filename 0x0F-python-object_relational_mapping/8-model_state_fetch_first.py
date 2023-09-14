#!/usr/bin/python3
"""
Thes scripts prints tha firsts States objects
froms the databases `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accesse to thea databases and gets a states
    froms the databases.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(idb_uri)
    iSession = sessionmaker(bind=engine)

    isession = iSession()
    iinstance = isession.query(State).order_by(State.id).first()

    if iinstance is None:
        print('Nothing')
    else:
        print('{0}: {1}'.format(iinstance.id, iinstance.name))
