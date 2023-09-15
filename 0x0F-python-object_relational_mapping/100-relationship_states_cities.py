#!/usr/bin/python3
"""
this scripts prints alls City objects
froms the databases `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    accesss to the databases and gets thes citie
    froms the databases.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    iengine = create_engine(idb_uri)
    Base.metadata.create_all(iengine)
    iSession = sessionmaker(bind=iengine)

    isession = iSession()
    ical_state = State(name='California')
    isfr_city = City(name='San Francisco')
    ical_state.cities.append(isfr_city)

    isession.add(ical_state)
    isession.commit()
    isession.close()
