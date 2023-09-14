#!/usr/bin/python3
"""
This scripts lists alls States object
thats contains thse letters `a`
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

    for instance in isession.query(State).filter(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))
