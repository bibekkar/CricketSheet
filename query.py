import yaml
import sqlite3
import os
from os import listdir


conn = sqlite3.connect('matchdata3.db')
db = conn.cursor()

# Get number of matches played by V Sehwag
matchIDs = []
db.execute("SELECT * FROM matchdata WHERE teamA='Delhi Daredevils' or teamB='Delhi Daredevils'")
rows = db.fetchall()
for r in rows:
	matchIDs.append(r[0])

c=0
for i in matchIDs:
	matchID = '\''+i+'\''
	db.execute("SELECT COUNT(*) FROM balls WHERE batsman='V Sehwag' and matchID="+matchID)
	rows = db.fetchall()
	for r in rows:
		print(r) 
		c=c+1
print(c)
db.close()