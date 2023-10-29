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

# create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS advanced_mathematics (
        LEA_STATE TEXT,
        LEA_STATE_NAME TEXT,
        LEAID TEXT,
        LEA_NAME TEXT,
        SCHID TEXT,
        SCH_NAME TEXT,
        COMBOKEY TEXT PRIMARY KEY,
        JJ TEXT,
        SCH_MATHCLASSES_ADVM TEXT,
        SCH_MATHCERT_ADVM TEXT,
        SCH_MATHENR_ADVM_HI_M TEXT,
        SCH_MATHENR_ADVM_HI_F TEXT,
        SCH_MATHENR_ADVM_AM_M TEXT,
        SCH_MATHENR_ADVM_AM_F TEXT,
        SCH_MATHENR_ADVM_AS_M TEXT,
        SCH_MATHENR_ADVM_AS_F TEXT,
        SCH_MATHENR_ADVM_HP_M TEXT,
        SCH_MATHENR_ADVM_HP_F TEXT,
        SCH_MATHENR_ADVM_BL_M TEXT,
        SCH_MATHENR_ADVM_BL_F TEXT,
        SCH_MATHENR_ADVM_WH_M TEXT,
        SCH_MATHENR_ADVM_WH_F TEXT,
        SCH_MATHENR_ADVM_TR_M TEXT,
        SCH_MATHENR_ADVM_TR_F TEXT,
        TOT_MATHENR_ADVM_M TEXT,
        TOT_MATHENR_ADVM_F TEXT,
        SCH_MATHENR_ADVM_LEP_M TEXT,
        SCH_MATHENR_ADVM_LEP_F TEXT,
        SCH_MATHENR_ADVM_IDEA_M TEXT,
        SCH_MATHENR_ADVM_IDEA_F TEXT
    )
''')

conn.commit()

# open the CSV file
with open('/Data/2017-18 Public-Use Files/Data/SCH/CRDC/CSV/Advanced Mathematics.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        # insert each row
        cur.execute(
            "INSERT INTO advanced_mathematics VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )

# commit the transaction
conn.commit()

# close the connection
cur.close()
conn.close()
