import yaml
import sqlite3

# Extracting the data from the file
data = {}
file = open("335982.yaml", "r")
data = yaml.load(file)

# Creating db
conn = sqlite3.connect('data.db')
db = conn.cursor()

try:
	# Creating table in db
	db.execute('''CREATE TABLE balls (innings INT, ball TEXT, bowler TEXT, batsman TEXT, extras INT, runs INT, total INT)''')
	
	# Stores ball-by-ball data for both innings
	innings = data['innings']
	first_innings = innings[0]['1st innings']
	second_innings = innings[1]['2nd innings']

	db.execute('''CREATE TABLE innings (inning TEXT, team TEXT)''')
	db.execute("INSERT INTO innings VALUES(?,?)", ('first',first_innings['team']))
	db.execute("INSERT INTO innings VALUES(?,?)", ('second',second_innings['team']))

	store(first_innings['deliveries'], 1, db)
	store(second_innings['deliveries'], 2, db)

	# Committing the changes made
	conn.commit()
except:
	print()

# Number of dot balls bowled by KKR

db.execute("SELECT * FROM innings WHERE team = 'Kolkata Knight Riders'")
rows = db.fetchall()
for r in rows:
	print(r)

# Querying the data
db.execute('SELECT * FROM balls')
rows = db.fetchall()
for r in rows:
	print(r)

conn.close()


def store(deliveries, innings, db):
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
			entries.add((innings,j,bowler,batsman,extras,runs,total))
	db.executeall("INSERT INTO balls VALUES (?,?,?,?,?,?,?)",entries)