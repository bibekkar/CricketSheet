import yaml
import sqlite3
import os
from os import listdir


conn = sqlite3.connect('matchdata2.db')
db = conn.cursor()
db.execute("SELECT * FROM balls WHERE runs=6 and bowler='P Kumar' and batsman='V Sehwag'")
rows = db.fetchall()
for r in rows:
	print(r)
db.close()