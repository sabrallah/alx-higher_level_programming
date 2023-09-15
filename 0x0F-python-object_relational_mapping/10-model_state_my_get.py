#!/usr/bin/python3
'''
print the State of object with who the name passed as an argument
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

    state = session.query(State).filter(State.name == argv[4]).first()
    print('Not found' if not state else state.id)
    session.close()
