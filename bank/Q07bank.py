import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT branch_city, COUNT(*) AS Count_Branch FROM branch_table GROUP BY branch_city")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)



