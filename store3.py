def store(deliveries, innings, db, matchID):
	entries = []
	for i in range(len(deliveries)):
		keys = deliveries[i].keys()
		for j in keys:
			ball = deliveries[i][j]
			bowler = ball['bowler']
			batsman = ball['batsman']
			runs = int(ball['runs']['batsman'])
			extras = int(ball['runs']['extras'])
			total = int(ball['runs']['total'])
			ball=j
			entries.append((matchID, innings,ball,bowler,batsman,extras,runs,total))
	db.executemany("INSERT INTO balls VALUES(?,?,?,?,?,?,?,?)",entries)

import yaml
import sqlite3


# Extracting the data from the file
data = {}
match = 335982
matchID = '335982'
file = open("data/"+matchID+".yaml", "r")
data = yaml.load(file)

# Creating db
conn = sqlite3.connect('matches3.db')
db = conn.cursor()

try:
	# Creating table in db

	db.execute('''CREATE TABLE matchdata (matchID TEXT, teamA TEXT, teamB TEXT)''')
	db.execute('''CREATE TABLE balls (matchID TEXT, innings INT, ball TEXT, bowler TEXT, batsman TEXT, extras INT, runs INT, total INT)''')


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
	print()

# Querying the data
db.execute('SELECT * FROM balls WHERE runs=6 AND innings=1')
rows = db.fetchall()
for r in rows:
	print(r)

conn.close()
