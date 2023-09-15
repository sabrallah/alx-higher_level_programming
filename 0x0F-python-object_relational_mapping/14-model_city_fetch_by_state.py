#!/usr/bin/python3
"""
This scripts print all Citys object
froms the databases `hbtn_0e_14_usa`.
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Acceses to the databases and gets the cities
    froms the databases.
    """

    idb_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    iengine = create_engine(idb_uri)
    iSession = sessionmaker(bind=iengine)

    isession = iSession()

    query = isession.query(City, State).join(State)

    for _c, _s in query.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))

    isession.commit()
    isession.close()
