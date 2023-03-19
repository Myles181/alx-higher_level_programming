#!/usr/bin/python3

"""
    Write a script that lists all
    State objects from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.ext.declaration import declaration_base
from sqlalchemy import create_engine, Column, Integer, String
from model_state import Base, State
from sqlalchemy import sessionmaker

Base = declaration_base()


class State(Base):
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=True)
    name = Column(String(128), nullable=True)

    engine = create_engine("mysql+mysqldb://{}:{}
                            @localhost/{}".format(username, password, database),
                            pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State_id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
