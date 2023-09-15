#!/usr/bin/python3
'''
print all the city of objects
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    insSession = sessionmaker(bind=engine)
    session = insSession()

    elements = session.query(State, City).join(City).order_by(City.id).all()
    for state, city in elements:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.close()
