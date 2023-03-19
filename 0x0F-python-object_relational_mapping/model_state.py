#!/usr/bin/python3

""" Write a python file that contains
    the class definition of a State
    and an instance Base = declarative_base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """ Link to table """
    __tablename__ = "states"

    """ Identify table's column """
    id = Column(Integer, autoincrement = True,
                primary_key = True, nullable = True)
    name = Column(String(128), nullable = True)
