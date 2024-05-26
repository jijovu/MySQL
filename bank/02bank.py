import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE branch_table(branch_id VARCHAR(255),\
                 branch_name VARCHAR(255),\
                 branch_city VARCHAR(255),\
                 PRIMARY KEY (branch_id))")