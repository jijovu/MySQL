import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mydatabase8"
)

print(mydb) 

mycursor =mydb.cursor()

#mycursor.execute("CREATE TABLE user (id VARCHAR(255),name VARCHAR(255),favorite VARCHAR(255))")
sql ="INSERT INTO user(id,name,favorite) VALUE (%s,%s,%s)"
val =[
    ("1","John","154"),
    ("2","Peter","154"),
    ("3","Hannah","")
]
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount," was inserted")






