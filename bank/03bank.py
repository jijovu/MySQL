import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE account_table(account_number VARCHAR(255),\
                 customer_id VARCHAR(255),\
                 branch_id VARCHAR(255),\
                 opening_balance VARCHAR(255),\
                 account_opening_date DATE ,\
                 account_type VARCHAR(255),\
                 account_status VARCHAR(255),\
                 PRIMARY KEY (account_number),\
                 FOREIGN KEY (customer_id) REFERENCES customer_table(customer_id),\
                 FOREIGN KEY (branch_id) REFERENCES branch_table(branch_id))")






