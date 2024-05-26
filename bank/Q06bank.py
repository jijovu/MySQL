import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ="root",
    database = "bank"

)

mycursor = mydb.cursor()

mycursor.execute("SELECT customer_table.first_name,\
                 customer_table.city,\
                 account_table.account_number \
                 FROM account_table  \
                 INNER JOIN customer_table ON account_table.customer_id =  customer_table.customer_id \
                 WHERE occupation NOT LIKE 'Python Developer' AND occupation NOT LIKE 'Electrical Engineer'\
                 AND occupation NOT LIKE 'Graphics Designer'\
                 AND occupation NOT LIKE 'Housewife'")

myresult = mycursor.fetchall()

for x in myresult :
    print(x)



