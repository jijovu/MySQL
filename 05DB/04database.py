import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "hospital"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE Doctor_table MODIFY COLUMN Doctor_Id INT, MODIFY COLUMN Join_Date DATE,MODIFY COLUMN Salary DECIMAL(10, 2),MODIFY COLUMN Experience INT")

mydb.commit()