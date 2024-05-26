import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "bank"
)

mycursor = mydb.cursor()

sql = "INSERT INTO transaction_details_table (transaction_number,account_number,date_of_transaction,medium_of_transaction,transaction_type,transaction_amount) VALUES (%s,%s,%s,%s,%s,%s)"

val = [
   ("T00001","A00007","2018-05-24","Cash","Deposit","4500"),
   ("T00002","A00005","2019-07-27","Cheque","Deposit","2000"),
   ("T00003","A00002","2020-10-11","Cash","Withdrawal","5000"),
   ("T00004","A00008","2020-12-09","Cash","Withdrawal","12000"),
   ("T00005","A00010","2021-04-22","Cheque","Deposit","5600"),
   ("T00006","A00001","2021-06-15","Cheque","Withdrawal","1400"),
   ("T00007","A00006","2021-09-12","Cash","Deposit","8000"),
   ("T00008","A00004","2022-07-25","Cheque","Deposit","6500"),
   ("T00009","A00003","2023-06-28","Cash","Withdrawal","5300"),
   ("T00010","A00009","2023-09-12","Cheque","Deposit","1600")
]

mycursor.executemany(sql,val)

mydb.commit()


