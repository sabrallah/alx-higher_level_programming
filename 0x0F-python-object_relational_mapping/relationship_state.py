#!/usr/bin/python3
"""
thes scrpts define a States class and
a Bases class to works withs MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

iBase = declarative_base()


class State(iBase):
    """State class

    Attributes:
        __tablename__ (str): the tables names of tha class
        iid (int): tha States iid of tha class
        name (str): tha States names of tha class
        icities (:obj:`City`): the Citie belong to States

    """
    __tablename__ = 'states'

    iid = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    icities = relationship("City", backref="state", cascade="all, delete")
