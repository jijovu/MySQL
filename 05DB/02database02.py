import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="hospital"
)

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE Doctor_table (Doctor_Id VARCHAR(255),Doctor_Name VARCHAR(255),Hospital_Id VARCHAR(255),Join_Date VARCHAR(255),Speciality VARCHAR(255),Salary VARCHAR(255),Experience VARCHAR(255))")

sql ="INSERT INTO Doctor_table (Doctor_Id,Doctor_Name,Hospital_Id,Join_Date,Speciality,Salary,Experience) VALUES (%s,%s,%s,%s,%s,%s,%s)"
val =[
    ("101","David","1","2005-02-10","Pediatric","40000",None),
    ("102","Michael","1","2018-07-23","Oncologist","20000",None),
    ("103","Susan","2","2016-05-19","Gamacologist","25000",None),
    ("104","Robert","2","2017-12-28","Pediatric","28000",None),
    ("105","Linda","3","2004-12-28","Gamacologist","42000",None),
    ("106","William","3","2012-09-11","Dermatologist","30000",None),
    ("107","Richard","4","2014-08-21","Garnacologist","32000",None),
    ("108","Karen","4","2011-11-17","Radilologist","30000",None)
]
mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount, "was inserted")





