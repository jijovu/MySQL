import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital"
)

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE hospital_table (Hospital_id VARCHAR(255),Hospital_name VARCHAR(255),Bed_count VARCHAR(255))")
sql ="INSERT INTO hospital_table(Hospital_id,Hospital_name,Bed_count) VALUE (%s,%s,%s)"
val =[("1","Mayo Clinic","200"),
      ("2","Cleveland Clinic","300"),
      ("3","Johns Hopkins","1000"),
      ("4","UCLA Medical Center","1500")
]
mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount, "was inerted")



