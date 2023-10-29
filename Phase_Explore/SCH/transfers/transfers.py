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

# Create table
cur.execute('''
    CREATE TABLE IF NOT EXISTS transfers(
        LEA_STATE TEXT,
        LEA_STATE_NAME TEXT,
        LEAID TEXT,
        LEA_NAME TEXT,
        SCHID TEXT,
        SCH_NAME TEXT,
        COMBOKEY TEXT,
        JJ TEXT,
        SCH_DISCWODIS_TFRALT_HI_M INT,
        SCH_DISCWODIS_TFRALT_HI_F INT,
        SCH_DISCWODIS_TFRALT_AM_M INT,
        SCH_DISCWODIS_TFRALT_AM_F INT,
        SCH_DISCWODIS_TFRALT_AS_M INT,
        SCH_DISCWODIS_TFRALT_AS_F INT,
        SCH_DISCWODIS_TFRALT_HP_M INT,
        SCH_DISCWODIS_TFRALT_HP_F INT,
        SCH_DISCWODIS_TFRALT_BL_M INT,
        SCH_DISCWODIS_TFRALT_BL_F INT,
        SCH_DISCWODIS_TFRALT_WH_M INT,
        SCH_DISCWODIS_TFRALT_WH_F INT,
        SCH_DISCWODIS_TFRALT_TR_M INT,
        SCH_DISCWODIS_TFRALT_TR_F INT,
        TOT_DISCWODIS_TFRALT_M INT,
        TOT_DISCWODIS_TFRALT_F INT,
        SCH_DISCWODIS_TFRALT_LEP_M INT,
        SCH_DISCWODIS_TFRALT_LEP_F INT,
        SCH_DISCWDIS_TFRALT_IDEA_HI_M INT,
        SCH_DISCWDIS_TFRALT_IDEA_HI_F INT,
        SCH_DISCWDIS_TFRALT_IDEA_AM_M INT,
        SCH_DISCWDIS_TFRALT_IDEA_AM_F INT,
        SCH_DISCWDIS_TFRALT_IDEA_AS_M INT,
        SCH_DISCWDIS_TFRALT_IDEA_AS_F INT,
        SCH_DISCWDIS_TFRALT_IDEA_HP_M INT,
        SCH_DISCWDIS_TFRALT_IDEA_HP_F INT,
        SCH_DISCWDIS_TFRALT_IDEA_BL_M INT,
        SCH_DISCWDIS_TFRALT_IDEA_BL_F INT,
        SCH_DISCWDIS_TFRALT_IDEA_WH_M INT,
        SCH_DISCWDIS_TFRALT_IDEA_WH_F INT,
        SCH_DISCWDIS_TFRALT_IDEA_TR_M INT,
        SCH_DISCWDIS_TFRALT_IDEA_TR_F INT,
        TOT_DISCWDIS_TFRALT_IDEA_M INT,
        TOT_DISCWDIS_TFRALT_IDEA_F INT,
        SCH_DISCWDIS_TFRALT_LEP_M INT,
        SCH_DISCWDIS_TFRALT_LEP_F INT,
        SCH_DISCWDIS_TFRALT_504_M INT,
        SCH_DISCWDIS_TFRALT_504_F INT
    )
''')

# Commit changes
conn.commit()

# Open and read the file
# open the CSV file
with open('C:/Users/evanj/OneDrive/Desktop/Programming/DataScience/Datathon_2023/Data/2017-18 Public-Use '
          'Files/Data/SCH/CRDC/CSV/Transfers.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row.
    for row in reader:
        # insert each row
        cur.execute(
            "INSERT INTO transfers VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, "
            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            row
        )
conn.commit()
