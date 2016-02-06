#edges = [(1,3),(2,3),(3,4),(4,5),(5,6),(6,7),(5,7),(3,5),(4,10),(3,10),(5,10),(5,8),(8,9),(8,10),(10,11)]

import psycopg2

# Connect to database
try:
    conn=psycopg2.connect("dbname='db15826' user='newuser' password='15826'")
except:
    print "I am unable to connect to the database."

cur = conn.cursor()
try:
    cur.execute("""SELECT * from test""")
except:
    print "I can't SELECT from test"

rows = cur.fetchall()

# Create adjacency matrix
adjm = dict()
for e in rows:
	if adjm.get(e[0]) == None:
		adjm[e[0]] = [e[1]]
	else:
		adjm[e[0]].append(e[1])

	if adjm.get(e[1]) == None:
		adjm[e[1]] = [e[0]]
	else:
		adjm[e[1]].append(e[0])

# initilize degree of all vertex
degree = dict((v, len(adjm[v])) for v in adjm)

# number of vertex
n = len(adjm)
output = list()

# create buckets that contain all vertex of degree i in bucket i
maxdegree = max(degree)
D = [[] for i in range(maxdegree+1)]
for (v, d) in degree.items():
	D[d].append(v)

# k is the coreness of the current node
k = 0

# Repeat n times:
# Scan buckets until find an i for which D[i] is nonempty
# Set k to max(k,i)
# Select a vertex v from D[i], k is the coreness, add (v,k) to output
# For each neighbor w of v not in output, subtract one from degree and move the node to the corresponding bucket
for i in range(n):
	for (i, di) in enumerate(D):
		if len(di) != 0:
			k = max(k,i)
			break;
	v = di[0]
	D[i].remove(v)
	degree[v] = 0
	output.append((v,k))
	for w in adjm[v]:
		if degree[w] > 0:
			D[degree[w]].remove(w)
			degree[w] -= 1
			D[degree[w]].append(w)
print output
	
cur.executemany("""INSERT INTO result(v,k) VALUES (%s, %s)""", output)
conn.commit()
conn.close()
