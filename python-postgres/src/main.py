import psycopg2
conection = psycopg2.connect(user="postgres",
                            password="123",
                            port="5432",
                            host="db",
                            database="persondb")
print(conection)
cursor = conection.cursor()
cursor.execute("INSERT INTO person(name, edad) VALUES (grace, 17);")
conection.commit()
cursor.close()
conection.close()