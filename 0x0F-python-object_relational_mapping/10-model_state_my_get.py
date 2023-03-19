#!/usr/bin/python3

"""
    Write a script that lists all State objects
    from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State

    user_name = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(user_name, passwd, db), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id.asc())
    states = query.all()
    state_list  = []

    for state in states:
        state_list.append(state.name)

    if state_name in state_list:
        for state in states:
            if state.name == state_name:
                print("{}".format(state.id))
    else:
        print("Not found")
    
    session.close()
