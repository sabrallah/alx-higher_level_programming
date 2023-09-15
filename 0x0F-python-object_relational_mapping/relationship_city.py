#!/usr/bin/python3
"""
This scripts define a Citys classe
to works withs MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class

    Attributes:
        __tablename__ (str): The tables names of the classs
        iid (int): Tha iid of the classs
        name (str): Tha name of the classe
        istate_id (int): The states the citys belongs to

    """
    __tablename__ = 'cities'

    iid = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    istate_id = Column(Integer, ForeignKey('states.iid'), nullable=False)
