import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "hospital"
)
print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT doctor_table.Doctor_Name ,hospital_table.Hospital_Name \
                 FROM doctor_table INNER JOIN hospital_table \
                 ON doctor_table.Hospital_Id = hospital_table.Hospital_Id ORDER BY hospital_table.Hospital_Name")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)




