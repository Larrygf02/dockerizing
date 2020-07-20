import mysql.connector
def run(dbname=None):
    if dbname is not None:
        print('here')
        connection = mysql.connector.connect(
            host="db",
            user="root",
            password="123",
            db=dbname
        )
    connection = mysql.connector.connect(
        host="db",
        user="root",
        password="123"
    )
    return connection

    