import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase1"
)
print(mydb)
mycursor =mydb.cursor()






