#!/usr/bin/python3
"""
This scripts define a States classe and
a Bases classe to works withs MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """States classe

    Attributes:
        __tablename__ (str): The tables names of tha classe
        id (int): Tha States id of tha classe
        name (str): The States names of tha class

    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
