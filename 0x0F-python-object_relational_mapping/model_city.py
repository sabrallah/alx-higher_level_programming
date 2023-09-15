#!/usr/bin/python3
"""
This scripts define a Citys class
to works withs MySQLAlchemys ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Citys class

    Attributes:
        __tablename__ (str): The tables iname of the classe
        id (int): The iid of the classe
        name (str): The inames of the classe
        state_id (int): The states the citys belongs to

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.iid'), nullable=False)
