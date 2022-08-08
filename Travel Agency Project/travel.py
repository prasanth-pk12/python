import mysql.connector as mc 
#connecting the database with the python
mydb=mc.connect(
    host="localhost",
    user="root",
    password="",
   database="tms"

)

#creating new login id and user name..
def create_account():
    cur=mydb.cursor()
    print("**************Create Account**************")
    user=int(input("Enter use user id : "))
    pas=input("Enter password : ")
    s="insert into user_info (user_id,password) values(%s,%s)"
    v=(user,pas)
    cur.execute(s,v)
    mydb.commit()
    print("Account created")
    print(f"User id : {user}\nPassword :{pas}")
# Login to the travel agency..    
def login():
    cur=mydb.cursor()
    user=int(input("Enter use user id : "))
    password=input("Enter password : ")
    cur.execute(f"select * from user_info where user_id={user} && password={'password'}")
    result=cur.fetchall()
    if len(result)==0:
        print("Sorry you don't have account \nPlease create a new account ")
        create_account()
    if len(result)==1:
        print("Login successful")
        for i in result:
            print(f"User id  :{user}")
            print(f"Password :{password}")

# Program for making a booking a new travel..
def make_travel():
    cur=mydb.cursor()
    print("**** HI WELCOME TO OUR TRAVEL AGENCY ****")
    print("\nPlease enter the following details to book the travel..")
    user=int(input("Enter use user id : "))
    user_name=input("Enter your name : ")
    f_place=input("Enter the starting place : ")
    t_place=input("Enter where you want to travel : ")
    dat = input("Enter the date of travel : ")
    t_state=input("Enter your travel status : ")
   
    s="insert into travel_details (user_id,user_name,from_where,to_where,dot,travel_status) values(%s,%s,%s,%s,%s,%s)"
    v=(user,user_name,f_place,t_place,dat,t_state)
   
    cur.execute(s,v)
    mydb.commit()
    print("\nYour travel booked successfully ...............")
    print("\nYour details are ::")
    print(f"User id        : {user}")
    print(f"User name      : {user_name}")
    print(f"From           : {f_place}")
    print(f"To             : {t_place}")
    print(f"Date of travel : {dat}")    
    print("Thank you for booking tarvel in our agency.")

# Program to postpone the booked travel..
def postpone_travel():
    cur=mydb.cursor()
    print("What is the reason of postponding ???")
    u=input("Enter your user id : ")
    en=input("Enter the reason of of postponding : ")
    print(f"Your reason of postponding {en} is accepted .")
    da=input("Enter the date you want to travel : ")
    s=f"update travel_details set dot={da} where user_id={u}"
    cur.execute(s)
    mydb.commit()
    print(f"Your tavel date postponed to {da}")  

# Program to cancle the booked travel..
def cancel_travel():
    cur=mydb.cursor()
    en=input("Enter your user id : ")
    s=f"delete from travel_details where user_id={en}"
    cur.execute(s)
    mydb.commit()
    print(f"Your tarvel has been cancelled succesfully...")  
    print()

# Program to show the travel history of user
def travel_history():
    print("{:<10}{:<12}{:<14}{:<14}{:<15}{:<14}".format("USER ID","USER NAME","FROM PLACE","TO PLACE","DATE","STATUS"))
    cur=mydb.cursor()
    s="select * from travel_details"
    cur.execute(s)
    f=cur.fetchall()
   
    for i in f:
        print("{:<10}{:<12}{:<14}{:<14}{:<15}{:<14}".format(i[0],i[1],i[2],i[3],i[4],i[5]))
            

while True:
    print()
    print("Enter 1 to Login.................................")
    print("Enter 2 to Create new account....................")
    print("Enter 3 to Make a new travel.....................")
    print("Enter 4 to postpone the booked travel............")
    print("Enter 5 to cancle the booked travel..............")
    print("Enter 6 to travel history........................")
    print("Enter 0 to exit..................................")
    print()
    try:
        choice=int(input("CHOICE  :  "))
        print()
        if(choice==1):
            login()
            pass
        elif(choice==2):
            create_account()
            pass
        elif (choice==3):
            make_travel()
            pass
        elif (choice==4):
            postpone_travel()
            pass
        elif choice==5:
            cancel_travel()
            pass
        elif choice==6:
            travel_history()
            pass
        elif choice==0:
            break
        else:
            print("Invalid choice given ...")
        
    except Exception as e:
        print(e)
        print("Invalid !! Try again")       
print()
print("Thank for visiting us ................")        
