import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE database9")








