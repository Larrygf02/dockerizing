import mysql.connector
connection = mysql.connector.connect(
            host="db",
            user="raul",
            password="123"
)
print(connection)