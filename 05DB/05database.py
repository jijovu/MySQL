import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "hospital"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE hospital_table MODIFY COLUMN Hospital_id INT,MODIFY COLUMN Bed_count INT")

mydb.commit()
