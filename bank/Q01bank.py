import mysql.connector

mydb = mysql.connector.connect (
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT customer_id, first_name, DOB FROM customer_table ORDER BY YEAR(DOB), first_name")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)