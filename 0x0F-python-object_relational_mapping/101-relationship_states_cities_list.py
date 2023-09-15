#!/usr/bin/python3
"""
lists alls States object and corresponding Citys object containeds in the DB
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    ist = session.query(State).outerjoin(City).order_by(State.id,
                                                        City.id).all()

    for istate in ist:
        print("{}: {}".format(istate.id, istate.name))
        for icity in istate.cities:
            print("    {}: {}".format(icity.id, icity.name))
