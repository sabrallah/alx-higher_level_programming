#!/usr/bin/python3
'''
change the name of State of object
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    insSession = sessionmaker(bind=engine)
    session = insSession()

    states = session.query(State).filter(State.id == 2)

    for el in states:
        el.name = 'New Mexico'

    session.commit()
    session.close()
