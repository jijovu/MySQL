import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase4"
)
print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase4")
#mycursor.execute(
#     "CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")

sql = "INSERT INTO customers(name,address) VALUES (%s, %s)"
val = [("John", "Highway 21"),
       ("Ben", "Highway 23"),
       ("Ben", "Highway 23"),
       ("Ben", "Highway 23"),
       ("Ben", "Highway 23"),
       ("Ben", "Highway 23"),
       ("Ben", "Highway 23")
       ]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")






