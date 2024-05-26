import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "hospital"
)
print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM doctor_table WHERE speciality = 'Dermatologist'")
#mycursor.execute("UPDATE doctor_table SET speciality = 'Gamacologist' WHERE speciality = 'Dermatologist'")
#mycursor.execute("DELETE FROM doctor_table WHERE speciality = 'Gamacologist'")

sql = "SELECT * FROM hospital_table ORDER BY Bed_count DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)




