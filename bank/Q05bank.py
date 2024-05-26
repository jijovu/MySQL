import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT customer_table.customer_id, customer_table.first_name, account_table.account_number\
                 FROM customer_table JOIN account_table ON customer_table.customer_id = account_table.customer_id \
                 WHERE DAY(account_table.account_opening_date) > 15")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

