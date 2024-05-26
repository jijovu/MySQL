import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="database9"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Customers (CustomerID VARCHAR(255),CustomerName VARCHAR(255),ContactName VARCHAR(255),Address VARCHAR(255),City VARCHAR(255),PostalCode VARCHAR(255),Country VARCHAR(255))")





