#!/usr/bin/python3

"""
    Write a script that lists all State objects
    with the character 'a' inside of it
    from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    import re
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
    states = query.all()

    for state in states:
        matches = re.findall(r'a', state.name)
        if matches:
            print("{}: {}".format(state.id, state.name))

    session.close()
