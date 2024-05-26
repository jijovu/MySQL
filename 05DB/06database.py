import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "hospital"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE hospital_table RENAME COLUMN Hospital_name TO Hospital_Name")

mydb.commit()


