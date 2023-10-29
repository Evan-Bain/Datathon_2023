import psycopg2
from psycopg2 import OperationalError


def create_conn():
    conn = None
    try:
        # Edit the connection parameters according to your setup
        conn = psycopg2.connect(
            database="testdb",
            user="postgres",
            password="evanbain",
            host="localhost",
            port="5432",
        )
        print("Successfully connected to the PostgreSQL database")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return conn


connection = create_conn()
