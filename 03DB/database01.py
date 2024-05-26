import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root"
    #database = "database8"
)

print(mydb)

mycursor =mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase8")