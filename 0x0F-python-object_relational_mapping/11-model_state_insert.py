#!/usr/bin/python3

"""
    Write a script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
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

    """ Create new class data """
    new = State(name="Loisiana")
    session.add(new)
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()

    print("{}".format(new_state.id))

    session.close()
