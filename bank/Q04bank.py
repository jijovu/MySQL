import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT COUNT(*) AS Cust_Count FROM customer_table WHERE city = 'Marayamuttom' ")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


