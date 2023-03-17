#!/usr/bin/python3

import MySQLdb
import sys

conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
        )
curr = conn.cursor()
curr.execute("SELECT * FROM states WHERE name LIKE 'N%'")
db = curr.fetchall()

for i in db:
    print(i)

curr.close()
