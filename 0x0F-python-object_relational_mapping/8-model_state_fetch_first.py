#!/usr/bin/python3

"""
    Write a script that lists first State objects
    from the database hbtn_0e_6_usa
    if column is empty print nothing
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user_name, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id.asc())
    states = query.first()

    if (states.id is not None) or (states.name is not None):
        print("{}: {}".format(states.id, states.name))
    else:
        print("")

    session.close()
