import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

sql = "INSERT INTO account_table (account_number,customer_id,branch_id,opening_balance,account_opening_date,account_type,account_status) VALUES (%s,%s,%s,%s,%s,%s,%s)"

val = [
    ("A00001","C00001","B00001","1000","2020-06-12","Saving","Active"),
    ("A00002","C00001","B00002","1000","2019-02-18","Saving","Active"),
    ("A00003","C00003","B00004","1000","2022-11-10","Saving","Active"),
    ("A00004","C00004","B00005","1000","2021-07-20","Saving","Active"),
    ("A00005","C00001","B00005","1000","2018-09-22","Saving","Suspended"),
    ("A00006","C00002","B00002","1000","2020-06-16","Saving","Terminated"),
    ("A00007","C00003","B00007","1000","2017-01-25","Saving","Active"),
    ("A00008","C00005","B00009","1000","2019-08-11","Saving","Suspended"),
    ("A00009","C00007","B00008","1000","2023-06-12","Saving","Terminated"),
    ("A00010","C00009","B00001","1000","2020-02-10","Saving","Active")
]

mycursor.executemany(sql,val)

mydb.commit()


