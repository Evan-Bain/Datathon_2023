# commit the transaction
import csv
import psycopg2

# establish a database connection
conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='evanbain',
    dbname='postgres'
)

# create a new cursor
cur = conn.cursor()

conn.commit()

# select data from table
cur.execute("SELECT * FROM advanced_mathematics")

# fetch all the rows
rows = cur.fetchall()

for row in rows:
    print(row)

# then you can close the connection and cursor
cur.close()
conn.close()