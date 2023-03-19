#!/usr/bin/python3

"""
    List all columns that name column starts from N
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
            )
    curr = conn.cursor()
    curr.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = curr.fetchall()

    for row in rows:
        print(row)

    curr.close()
    conn.close()
