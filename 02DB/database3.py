import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase7"
    )
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM mytable1 LIMIT 4 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)







