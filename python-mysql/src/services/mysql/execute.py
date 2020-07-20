import mysql.connector
from .connection import run as create_connection
def run(query, dbname=None):
    connection = create_connection(dbname)
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    connection.close()