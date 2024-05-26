import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT account_table.account_number,account_table.customer_id , \
                 customer_table.first_name ,customer_table.last_name ,account_table.account_opening_date\
                 FROM customer_table INNER JOIN account_table\
                 ON customer_table.customer_id = account_table.customer_id")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


