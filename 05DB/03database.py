import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "hospital"
)

mycursor = mydb.cursor()

mycursor.execute("UPDATE doctor_table SET Join_date = '2017-12-28' WHERE Doctor_Name ='Robert'")

mydb.commit()


