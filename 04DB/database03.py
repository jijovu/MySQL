import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="database9"
)

print(mydb)

mycursor = mydb.cursor()

sql = "INSERT INTO customers(CustomerID,CustomerName,ContactName,Address,City,PostalCode,Country) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
val = [("1","Alfreds Futterkiste","Maria Anders","Obere Str. 57","Berlin","12209","Germany"),
       ("2","Ana Trujillo Emparedados y helados","Ana Trujillo","Avda. de la Constitución 2222","México D.F.","05021","Mexico"),
       ("3","Antonio Moreno Taquería","Antonio Moreno","Mataderos 2312","México D.F.","05023","Mexico")]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount," was inserted")