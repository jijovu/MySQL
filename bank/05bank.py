import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bank"
)

mycursor = mydb.cursor()
 
sql = "INSERT INTO customer_table (customer_id, full_name, middle_name, last_name, city, mobile_number, occupation, DOB) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

val = [
    ("C00001", "Sree", "Reshmi", "Nair", "Trivandrum", "8979654378", "Housewife", "2000-02-23"),
    ("C00002", "Abhijith", "A", "S", "Neyyatinkara", "9846758496", "Python Developer", "2000-12-22"),
    ("C00003", "Ajay", "S", "H", "Marthandam", "7864546738", "Python Developer", "2000-08-06"),
    ("C00004", "Rahul", "Sanal", "S", "Marayamuttom", "7854673567", "Python Developer", "2000-04-05"),
    ("C00005", "Aswathy", "S", "H", "Marthandam", "8976564879", "Python Developer", "2000-08-14"),
    ("C00006", "Dayana", "Mariyam", "John", "kollam", "9877657445", "Python Developer", "2000-10-12"),
    ("C00007", "Arun", None, "M", "Marayamuttom", "9877678453", "Electrical Engineer", "2000-05-15"),
    ("C00008", "Abhay", "Chandran", "JK", "Keezharoor", "8966546373", "Electrical Engineer", "2000-07-26"),
    ("C00009", "Vishnudas", "S", "K", "Marayamuttom", "8876547859", "Graphics Designer", "2000-08-14"),
    ("C00010", "Amal", None, "Dev", "Marayamuttom", "8967456388", "Game Developer", "2000-06-04")
]

mycursor.executemany(sql, val)

mydb.commit()
# print(mycursor.rowcount, "records inserted.")
