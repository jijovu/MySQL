import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "mydatabase8"
)

print(mydb) 

mycursor =mydb.cursor()

sql = "SELECT \
user.name AS user, \
products.name AS products \
FROM user \
INNER JOIN products ON users.favourite = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)




