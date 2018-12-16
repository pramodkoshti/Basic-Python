import mysql.connector

myDbConnection = mysql.connector.connect(
	host = "localhost",
	user = "pramod",
	password = "Tfgh5671@",
	database = "Practice"
	)

"""print(myDbConnection)


db_cursor = myDbConnection.cursor()

db_cursor.execute("CREATE DATABASE Practice;")

db_cursor.execute("SHOW DATABASES")

for x in db_cursor:
	print(x)"""

db_cursor = myDbConnection.cursor()

#db_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Pramod", "Pune 57")

db_cursor.execute(sql,val)

myDbConnection.commit()

print(db_cursor.rowcount, " records inserted")

db_cursor.execute("Select * from customers")	