import sqlite3
 
connection_obj = sqlite3.connect('covid19.database.db')
 
cursor_obj = connection_obj.cursor()

cursor_obj.execute("DROP TABLE IF EXISTS DATA")
 
table = """ CREATE TABLE covid19_vaccine (
            ADHAAR_NUMBER int UNIQUE NOT NULL,
            First_Name CHAR(25) NOT NULL,
            Last_Name char(10),
            Phone_Number int not null,
            Age int,
            Doses int
        ); """
#cursor_obj.execute(table)  

while True:
    
    Adhaar_number = (input("Enter your Adhaar number: "))
    if len(str(Adhaar_number)) < 12:
        print("Enter valid Adhaar number")
        continue
    First_name = input("Enter your First name: ")
    Last_name = input("Enter your Last name: ")
    Age = input("Enter your age: ")
    phone_number = input("enter the phone number:  ")
    if len(str(phone_number)) < 10:
        print("Enter valid phone number")
        continue
    doses = int(input("how many doses have you completed?: "))
    if doses > 2:
        print("Enter the valid dose number")
        continue

    sql = "insert into covid19_vaccine(Adhaar_number,First_name,Last_name,Age,phone_number,doses) values (?, ? ,? ,? ,? ,? );"
    cursor_obj.execute(sql,(Adhaar_number,First_name,Last_name,Age,phone_number,doses))
    connection_obj.commit()
    data=cursor_obj.execute('''SELECT * FROM covid19_vaccine''')
    for row in data:
        print(row)