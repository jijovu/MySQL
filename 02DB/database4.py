import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mydatabase7"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE mytable2 (name VARCHAR(255),addresss VARCHAR(255))")

sql ="INSERT INTO mytable2(name,addresss) VALUES (%s,%s)"
val =[("John", "Highway 21"),
      ("Ben","Highway 24")
      ]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")





