import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE transation_details_table(transaction_number VARCHAR(255),\
                 account_number VARCHAR(255),\
                 date_of_transaction VARCHAR(255),\
                 medium_of_transaction VARCHAR(255),\
                 transaction_type VARCHAR(255),\
                 transaction_amount VARCHAR(255),\
                 FOREIGN KEY (account_number) REFERENCES account_table(account_number))")








