import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mydatabase6"
)

mycursor = mydb.cursor()

# mycursor.execute("SELECT name FROM mytable")
# myresult = mycursor.fetchall()
# mycursor.execute("SELECT * FROM mytable")
# myresult = mycursor.fetchone()
# mycursor.execute("SELECT * FROM mytable WHERE name = 'Ben'")
mycursor.execute("SELECT * FROM mytable WHERE address LIKE '%Sky%' ")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
