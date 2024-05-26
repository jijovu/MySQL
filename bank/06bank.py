import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank"
)

mycursor = mydb.cursor()

sql = "INSERT INTO branch_table (branch_id,branch_name,branch_city) VALUES (%s,%s,%s)"
val = [
    ("B00001","Valiyavila","Trivandrum"),
    ("B00002","Gazipur","Delhi"),
    ("B00003","Poojapura","Trivandrum"),
    ("B00004","Edapally","Kochi"),
    ("B00005","Dadar West","Mumbai"),
    ("B00006","Alamcode","Trivandrum"),
    ("B00007","Anna Nagar","Chennai"),
    ("B00008","Balaramapuram","Trivandrum"),
    ("B00009","Nahur West","Mumbai"),
    ("B00010","Kodambakkam","Chennai"),
    ]

mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"records inserted")
