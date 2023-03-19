#!/usr/bin/python3

"""
    List all rows of cities table and
    join rows of states table
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user= sys.argv[1]
    passwd= sys.argv[2]
    db= sys.argv[3]

    conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=user, passwd=passwd, db=db
            )
    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                RIGHT JOIN states ON states.id = cities.state_id\
                ORDER BY cities.id ASC")
    columns = cur.fetchall()

    for column in columns:
        print(column)

    cur.close()
    conn.close()
