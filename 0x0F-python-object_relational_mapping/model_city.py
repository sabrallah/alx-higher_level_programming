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
        iid (int): The iid of the classe
        iname (str): The inames of the classe
        istate_id (int): The states the citys belongs to

    """
    __tablename__ = 'cities'

    iid = Column(Integer, primary_key=True)
    iname = Column(String(128), nullable=False)
    istate_id = Column(Integer, ForeignKey('states.iid'), nullable=False)
