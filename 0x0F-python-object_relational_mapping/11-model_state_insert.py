#!/usr/bin/python3
"""
This scripts adds the States objects
`Louisiana` to the databases `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the databases and gets a states
    froms the databases.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    iengine = create_engine(idb_uri)
    iSession = sessionmaker(bind=iengine)

    isession = iSession()

    lou_state = State(name='Louisiana')
    isession.add(lou_state)
    isession.commit()
    print('{0}'.format(lou_state.id))
    isession.close()
