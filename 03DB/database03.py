import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mydatabase8"
)

print(mydb) 

mycursor =mydb.cursor()

#mycursor.execute("CREATE TABLE products (id VARCHAR(255),name VARCHAR(255))")
sql ="INSERT INTO products (id,name) VALUE (%s,%s)"
val =[
    ("154","Chocolate Heaven"),
    ("155","Tasty Lemons"),
    ("156","Vanilla Dreams")
]
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount," was inserted")