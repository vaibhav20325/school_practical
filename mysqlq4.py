import mysql.connector
connection = mysql.connector.connect(host='localhost',
                                   database='database1',
                                   user='root',
                                   password='amity')
cursor = connection.cursor()
def insert():
    r=int(input('Enter RollNo: '))
    n=input('Enter Name: ')
    c=int(input('Enter Class: '))
    dob=int(input('Enter DOB: '))
    g=input('Enter Gender: ')
    
    query = "INSERT INTO student values('%d', '%s', '%d', '%d', '%s');" % (r,n,c,dob,g)
    cursor.execute(query)
    connection.commit()

def updaterecord():
    r=int(input('Enter RollNo to be updated: '))
    n=input('Enter Name: ')
    c=int(input('Enter Class: '))
    dob=int(input('Enter DOB: '))
    g=input('Enter Gender: ')
    
    query = query = "UPDATE student set Name='%s',Class='%d',DOB='%d',Gender='%s' where RollNo='%d';" % (n,c,dob,g,r)
    cursor.execute(query)
    connection.commit()
    
a=None
while a != "exit":
    a = input("Insert record/Update record/Exit: ").lower()
    if a == "insert":
        insert()
    elif a == "update":
        updaterecord()
