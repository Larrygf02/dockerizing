import mysql.connector
connection = mysql.connector.connect(
            host="ddd",
            user="root",
            password="123",
            db="persodb"
)
print(connection)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE persondb")
connection.close()
cursor.close()