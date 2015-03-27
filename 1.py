import yaml
import sqlite3

def store(deliveries, table, db):
	for i in range(len(deliveries)):
		keys = deliveries[i].keys()
		for j in keys:
			ball = deliveries[i][j]
			bowler = ball['bowler']
			batsman = ball['batsman']
			runs = int(ball['runs']['batsman'])
			extras = int(ball['runs']['extras'])
			total = int(ball['runs']['total'])
			# Inserting the data into the table
			db.execute("INSERT INTO " + table+ " VALUES (?,?,?,?,?,?)",(j,bowler,batsman,extras,runs,total))



# Extracting the data from the file
data = {}
file = open("335982.yaml", "r")
data = yaml.load(file)

# Creating db
conn = sqlite3.connect('data.db')
db = conn.cursor()

try:
	# Creating table in db

	db.execute('''CREATE TABLE first (ball TEXT, bowler TEXT, batsman TEXT, extras INT, runs INT, total INT)''')
	db.execute('''CREATE TABLE second (ball TEXT, bowler TEXT, batsman TEXT, extras INT, runs INT, total INT)''')
	
	# Stores ball-by-ball data for both innings
	innings = data['innings']
	first_innings = innings[0]['1st innings']
	second_innings = innings[1]['2nd innings']

	db.execute('''CREATE TABLE innings (inning TEXT, team TEXT)''')
	db.execute("INSERT INTO innings VALUES(?,?)", ('first',first_innings['team']))
	db.execute("INSERT INTO innings VALUES(?,?)", ('second',second_innings['team']))

	# Stores deliveries for first innings 
	deliveries = first_innings['deliveries']
	store(deliveries, 'first', db)

	# Stores deliveries for second innings
	deliveries = second_innings['deliveries']
	store(deliveries, 'second', db)

	# Committing the changes made
	conn.commit()
except:
	print()

# Number of dot balls bowled by KKR

db.execute("SELECT * FROM innings WHERE team = 'Kolkata Knight Riders'")
rows = db.fetchall()
for r in rows:
	print(r)

inning = r[0]

# Querying the data
db.execute('SELECT COUNT(*) FROM ' + inning +' WHERE runs=0')
rows = db.fetchall()
for r in rows:
	print(r)

conn.close()