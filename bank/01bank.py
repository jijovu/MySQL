import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE bank")

mycursor.execute("CREATE TABLE Customer_table (customer_id VARCHAR (255),\
                 full_name VARCHAR(255),\
                 middle_name VARCHAR(255),\
                 last_name VARCHAR(255),\
                 city VARCHAR(255),\
                 mobile_number VARCHAR(255),\
                 occupation VARCHAR(255),\
                 DOB VARCHAR(255),PRIMARY KEY (customer_id))")





