import datetime
import mysql.connector

# DB connection
myDb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "",
database = 'college'
)
myCursor = myDb.cursor()

# Student functionality
def student():
    user_name=input("Enter the student id : ")
    password=input("Enter the password: ")
    myCursor.execute(f"select * from stuinfo where regno={user_name} && password='{password}'")
    myResult = myCursor.fetchall()
    for i in myResult:
        print(f"\n*****************************")
        print(f"Regno      : {i[0]}" )
        print(f"Name       : {i[2]}" )
        print(f"department : {i[3]}" )
        print(f"year       : {i[4]}" )
        print(f"address    : {i[5]}" )
        print("\n******************************")

        change_password=input("Do you want to change your password? YES|NO : ")
        try:
            if(change_password.lower()== 'yes'):
                new_password=input("Enter your new password : ")
                myCursor.execute(f"UPDATE stuinfo SET password= %s where regno=%s && password=%s",(new_password,user_name,password))
                print("Your password updated successfully")
                myDb.commit()
            else:
                print("You didn't change your password and it remains the same")
                print("\n*****************************")
        except:
            Print("Please enter a valid answer")
        
# Staff functionality
def staff():
    user_name=input("Enter the staff id: ")
    password=input("Enter the password: ")
    myCursor.execute(f"select * from staffinfo where staffid={user_name} && password='{password}'")
    myResult = myCursor.fetchall()
    for i in myResult:
        print(f"\n******************************")
        print(f"Staff id   : {i[0]}" )
        print(f"Name       : {i[2]}" )
        print(f"department : {i[3]}" )
        print(f"address    : {i[4]}" )
        print("\n*******************************")
    
    q1 = int(input("Enter 1 to add new student : "))
    try:
        if q1==1:
            sid = input("Enter the student id : ")
            password = input("Enter the password : ")
            s_name = input("Enter student name : ")
            department = input("Enter the department : ")
            year = input("Enter the year : ")
            address = input("Enter the address : ")

            sql = "insert into stuinfo(regno,password,name,department,year,address) values(%s,%s,%s,%s,%s,%s)"
            val = (sid,password,s_name,department,year,address);

            myCursor.execute(sql,val)
            myDb.commit()

            print(f"{s_name} details are added.")
        
        else:
            print("No new students are added")
            print("\n*****************************")
    except:
        print("Please enter a valid number")


# principal funcionality
def principal():
    user_name=input("Enter the principal id : ")
    password=input("Enter the password: ")
    myCursor.execute(f"select * from princeinfo where princeid={user_name} && password='{password}'")
    myResult = myCursor.fetchall()
    for i in myResult:
        print(f"\n***************************")
        print(f"Principal ID  : {i[0]}" )
        print(f"Name          : {i[2]}" )
        print(f"department    : {i[3]}" )
        print(f"address       : {i[4]}" )
        print("*****************************")

    q1 = int(input("Enter 1 to add new staff : "))
    try:
        if q1==1:
            staffid = input("Enter the staff id : ")
            password = input("Enter the password : ")
            name = input("Enter staff name : ")
            department = input("Enter the department : ")
            address = input("Enter the address : ")

            sql = "insert into staffinfo(staffid,password,name,department,address) values(%s,%s,%s,%s,%s)"
            val = (staffid,password,name,department,address);

            myCursor.execute(sql,val)
            myDb.commit()

            print(f"{name} details are added.")
        
        else:
            print("No new staffs are added")
            print("\n*****************************")
    except:
        print("please enter a valid number")


    q1 = int(input("Enter 1 to add new course : "))
    try:
        if q1==1:
            cid = input("Enter the course id : ")
            cname = input("Enter course name : ")
            duration = input("Enter the duration : ")
            placements = input("Placement availability : ")
            hod = input("Enter the HOD name : ")

            sql = "insert into courseinfo(courseid,name,duration,placements,HOD) values(%s,%s,%s,%s,%s)"
            val = (cid,cname,duration,placements,hod);

            myCursor.execute(sql,val)
            myDb.commit()

            print(f"{cname} details are added.")
        
        else:
            print("No new courses are added")
            print("\n*****************************")
    except:
        print("Please enter a valid number")


# course functionality
def course():
    print("Course details")
    course_name=input("Enter the course id : ")
    myCursor.execute(f"select * from courseinfo where courseid={course_name}")
    myResult = myCursor.fetchall()
    for i in myResult:
        print(f"\n******************************************")
        print(f"Course ID                : {i[0]}" )
        print(f"Course Name              : {i[1]}" )
        print(f"Duration                 : {i[2]}" )
        print(f"Placements availability  : {i[3]}" )
        print(f"HOD                      : {i[4]}" )
        print("\n*******************************************")

date = datetime.datetime.now()
print("****************** College Database Management System ******************") 

print(f"\nToday Date : {f'{date}'[:10]}")
print(f"Current Time : {f'{date}'[11:16]} ")

def manage():
 
 print("\nEnter 1 to view student details : ")
 print("Enter 2 to view staff details : ")
 print("Enter 3 to view course details : ")
 print("Enter 4 to view admin details : ")
 try:
  ask = int(input("\nEnter your choice :"))
 except:
    print("\nPlease enter number only...🙏🏻")

 if(ask == 1):
    student()
    manage()
 if(ask==2):
    staff()
    manage()
 if(ask==3):
    principal()
    manage()
 if(ask==4):
    course()
    manage()
 if(ask>4):
    print("Enter value from 1 to 4 ")
    manage()

manage()
