import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT customer_id,first_name,\
  COALESCE(middle_name, last_name) AS Cust_Name FROM customer_table")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)