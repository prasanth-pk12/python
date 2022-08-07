import os
import mysql.connector as db
from twilio.rest import Client
from dotenv import load_dotenv
import random
import  datetime 

# DB connection
load_dotenv()
mydb = db.connect(
host = os.getenv("HOST"),
user = os.getenv("DB_USER"),
password = os.getenv("PASSWORD"),
database = 'covid_reg'
)
myCursor = mydb.cursor()

account_sid = 'AC2266a47ea7bcdb9a299155c6de877e8a'
auth_token = '6ebd7a39565148c8e2efb5e0ebb5574e'
client = Client(account_sid, auth_token)


# msg
def sendmsg(mob, no):
  client.messages.create(
                      from_='+14194064359',
                      to=f'+91{mob}',
                      body=f'Your OTP is {no}'
                      )
  print(f"\nOTP sent successfully to your mobile number {mob}. Check your messages.\n")


# random number generation
def rand_no():
    return  random.randint(9999, 100000)


# login
def login():
  # inside function
  def check(mob_no):
    
      myCursor.execute(f"select * from register where mob='{mob_no}' ")
      myresult = myCursor.fetchall()
      if len(myresult[0]) !=0:
       print(f"\nAdar no         : {myresult[0][0]}")
       print(f"Name            : {myresult[0][1]}")
       print(f"DOB             : {myresult[0][2]}")
       print(f"Registered date : {myresult[0][6]}")
       print(f"Hospital        : {myresult[0][7]} GH ")
      else: 
       print("Sorry you have not registered.")
       ask = input("Do you want to register ? YES | NO : ")
       if ask.lower() == 'yes':
        register()
       else:
        login()

  print("sellfregistration.cowin.giv.in")
  print("Log in using your mobile number : ")
  print("\nIt is a trial account. Please Enter this number only : 9360985793\n")
  mob_no = input("Enter your Number : ")
  
  if mob_no == '9360985793':
   rand =  rand_no()
   sendmsg(mob_no , rand)
   otp = int(input("Enter  OTP to verify : "))
   if rand == otp :
    check(mob_no)
  else:
    check(mob_no)
  


# register
def register():
  print("********************* Vaccine Registration Form *********************")
  adar = input("Enter your Adar number : ")
  name = input("Enter your name : ")
  dob = input("Enter your Date of birth : ")
  city =input("Enter your nearby GH location : ")
  date = f'{datetime.datetime.now()}'[0:10]
  mob = input('Enter mobile number : ')
  dose1='yes'
  dose2= ''
  
  if(mob == '9360985793'):
      rand =  rand_no()
      sendmsg(mob , rand)
      otp = int(input("Enter OTP to verify your number :"))
      if otp == rand:
        print("\nYou have successfully registered for vaccine.")
        f=open(f'{name}.pdf', 'x')
        f.write("")
        print("****************************************************************************************************")
        print(f"You can get your registered form here : {os.getcwd()}/{name}.pdf")
        print("****************************************************************************************************")
      else:
        print("Invalid OTP") 
  else:
        print("\nYou have successfully registered for vaccine.")
        f=open(f'{name}.pdf', 'x')
        f.write(f"{name} you have successfully registered for vaccine.\nDose : 1 \nLocation : {city} \nDate : {date}")
        print("****************************************************************************************************")
        print(f"You can get your registered form here : {os.getcwd()}/{name}.pdf")
        print("****************************************************************************************************")

  myCursor.execute('insert into register(adar,name,dob,dose1, dose2,date,mob,city) values(%s,%s,%s,%s,%s,%s,%s,%s)', (adar,name,dob,dose1, dose2,date,mob,city))
  mydb.commit()

  
# vaccine 
def vaccine():
  
  print("Enter 1 to register : ")
  print("Enter 2 to login : ")

  try:
     ask = int(input("Enter your choice : "))
     if ask == 1:
       register()
       login()
       import covid19
     elif ask == 2:
      login()
      import covid19
     else:
      print("\nPlease enter 1 or 2 only...🙏️\n")
      vaccine()
  except:
    print("\nPlease enter number only... 🙏️\n")
    vaccine()

  

 

 






