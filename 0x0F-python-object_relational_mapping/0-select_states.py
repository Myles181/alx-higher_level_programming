#!/usr/bin/python3

"""
    List all columns of state by ascending order of their id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """ Connect to sql server """
    conn = MySQLdb.connect(
            host="localhost", port=3306, user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3]
            )

    """ Create a cursor object """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
