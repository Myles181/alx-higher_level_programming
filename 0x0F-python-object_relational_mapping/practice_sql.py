#!/usr/bin/python3

import MySQLdb

db = MySQLdb.connect(host=5036f66a0329, user="root@5036f66a)
cur = db.cursor()

cur.execute(" CREATE TABLE song ( id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, title TEXT NOT NULL )")
