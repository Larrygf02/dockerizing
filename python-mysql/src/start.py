import mysql.connector
connection = mysql.connector.connect(
            host="ddd",
            user="root",
            password="123",
            db="persondb"
)
print(connection)
cursor = connection.cursor()
cursor.execute("INSERT INTO person(name, edad) VALUES (raul, 17)")
connection.close()
cursor.close()