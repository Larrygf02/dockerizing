import mysql.connector
connection = mysql.connector.connect(
            host="127.0.0.1",
            user="raul",
            password="123"
)
print(connection)