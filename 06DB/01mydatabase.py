import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase9 ")
# mycursor.execute("CREATE TABLE mytable01(column1 VARCHAR(255),column2 VARCHAR(255))")

mycursor.execute("ALTER TABLE customer_table CHANGE full_name first_name VARCHAR(255) ")

#mycursor.execute("UPDATE customer_table SET city = 'Balaramapuram' WHERE first_name = 'Amal'")

mydb.commit()



