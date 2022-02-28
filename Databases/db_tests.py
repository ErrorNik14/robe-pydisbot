import sqlite3

connection = sqlite3.connect("Databases/Economy.db")

crsr = connection.cursor()

crsr.execute("SELECT saddle FROM userinfo WHERE id=9090123892983")

record = crsr.fetchone()

print(record[0])

connection.close()