import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase7"
    )
print(mydb)
mycursor = mydb.cursor()


# sql="DELETE FROM mytable1 WHERE address = 'valley 345'"
# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")

#mycursor.execute("CREATE TABLE mytable1(name VARCHAR (255),address VARCHAR (255))")

sql ="UPDATE mytable1 SET address = %s WHERE address = %s "
val =("canyon 123","Valley 311")

mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")







