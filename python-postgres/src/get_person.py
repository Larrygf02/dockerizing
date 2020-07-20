import psycopg2
conection = psycopg2.connect(user="postgres",
                            password="123",
                            port="5432",
                            host="db",
                            database="persondb")
print("connetion")
print(conection)
cursor = conection.cursor()
cursor.execute("SELECT * from person")
row = cursor.fetchone()
print(row)
cursor.close()
conection.close()