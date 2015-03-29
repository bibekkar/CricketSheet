def store(deliveries, innings, db, matchID):
	entries = []
	wickets = []
	for i in range(len(deliveries)):
		keys = deliveries[i].keys()
		for j in keys:
			ball = deliveries[i][j]
			bowler = ball['bowler']
			batsman = ball['batsman']
			runs = int(ball['runs']['batsman'])
			extras = int(ball['runs']['extras'])
			total = int(ball['runs']['total'])
			if 'wicket' in ball:
				wicket = ball['wicket']
				player = wicket['player_out']
				kind = wicket['kind']
				ball=j
				wickets.append((matchID, innings, ball, bowler, player, kind))
			ball=j
			entries.append((matchID, innings,ball,bowler,batsman,extras,runs,total))
	db.executemany("INSERT INTO balls VALUES(?,?,?,?,?,?,?,?)",entries)
	db.executemany("INSERT INTO wickets VALUES(?,?,?,?,?,?)",wickets)

import yaml
import sqlite3
import os
from os import listdir
data = os.listdir("data/")

try:
		# Creating db
		conn = sqlite3.connect('matchdata3.db')
		db = conn.cursor()
		# Creating table in db
		db.execute('''CREATE TABLE matchdata (matchID TEXT, teamA TEXT, teamB TEXT)''')
		db.execute('''CREATE TABLE balls (matchID TEXT, innings INT, ball TEXT, bowler TEXT, batsman TEXT, extras INT, runs INT, total INT)''')
		db.execute('''CREATE TABLE wickets (matchID TEXT, innings INT, ball TEXT, bowler TEXT, player TEXT, kind TEXT)''')
except:
		flag = True

for i in data:
	try:
		matchID = i
		file = open("data/"+matchID, "r")
		data = yaml.load(file)

		# Stores ball-by-ball data for both innings
		innings = data['innings']
		first_innings = innings[0]['1st innings']
		second_innings = innings[1]['2nd innings']

		db.execute("INSERT INTO matchdata VALUES(?,?,?)", (matchID,first_innings['team'],second_innings['team']))

		store(first_innings['deliveries'], 1, db, matchID)
		store(second_innings['deliveries'], 2, db, matchID)

		# Committing the changes made
		conn.commit()
	except:
		print("Exception occured")

conn.close()