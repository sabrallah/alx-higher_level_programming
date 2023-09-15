#!/usr/bin/python3
"""
lister all States objects and corresponding City object contain in database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    ieng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(ieng)
    Session = sessionmaker(bind=ieng)
    session = Session()
    rows = session.query(State).all()
    for istate in rows:
        print("{}: {}".format(istate.id, istate.name))
        for icity in istate.cities:
            print("    {}: {}".format(icity.id, icity.name))
    session.close()
