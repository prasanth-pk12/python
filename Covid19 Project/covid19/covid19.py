import requests
import http.client
import json
from dotenv import load_dotenv
import os
import vaccine

#world level active cases
def worldCases():
  print("******************* Corona Virus Latest Update *******************\n")
  # API connection
  
  conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")
  headers = {
  'x-rapidapi-host': "covid-193.p.rapidapi.com",
  'x-rapidapi-key':  'ce19d0164fmsh3d383efc0e85ce5p16dcb1jsnb1a4a3c79541'
  }

  country = input("Enter country :  ")
  conn.request("GET", f"/statistics?country={country}", headers=headers)
  res = conn.getresponse()
  data = json.load(res)

  print('\n*******************************************************************')

  print(f"Date       : {data['response'][0]['time'][0:10]}" )
  print(f"Country    : {data['response'][0]['country']}")
  print(f"Population : {data['response'][0]['population']}")
  print(f"New        : {data['response'][0]['cases']['new']}")
  print(f"Active     : {data['response'][0]['cases']['active']}")
  print(f"Critical   : {data['response'][0]['cases']['critical']}")
  print(f"Recovered  : {data['response'][0]['cases']['recovered']}")

  cases = f"{data['response'][0]['cases']['active']}"

  if(int(cases)>200000):
   print("\nCorona is spreading rapidly. Stay home stay safe.  😷️")
   print("*******************************************************************")
  else:
    print("\nCorona cases are decreasing...Don't worry. Be safe and wear mask 😷️")
    print("*******************************************************************")


# India active cases : 
def indiaCases():

  url = "https://api.rootnet.in/covid19-in/stats/latest"

  payload={}
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)
  data = response.json()

  print("\n----------------------------------------------------Corona cases live update-------------------------------------------------------\n")
  print(f"Country                  : India")
  print(f"Total                    : {data['data']['summary']['total']}")
  print(f"Confirmed Cases Indian   : {data['data']['summary']['confirmedCasesIndian']}")
  print(f"Confirmed Cases Foreign  : {data['data']['summary']['confirmedCasesForeign']}")
  print(f"Discharged               : {data['data']['summary']['discharged']}")
  print(f"Deaths                   : {data['data']['summary']['deaths']}\n\n")

  # print state wise
  print("-------------------------------------------------State wise corona cases details--------------------------------------------------\n")

  print ("{:<5} {:<25} {:<25}  {:<25} {:<15} {:<15} {:<10}".format('No','State','ConfirmedCasesIndian', 'ConfirmedCasesForeign','Discharged', 'Deaths', 'Total'))

  print ("{:<5} {:<25} {:<25}  {:<25} {:<15} {:<15} {:<10}".format('---','--------------------','--------------------', '---------------------','--------------', '--------------', '-------------'))

  i=0
  while i<36:
    state = data['data']['regional'][i]['loc']
    if state =='Andaman and Nicobar Islands':
        state = state[0:20]
    if state =='Dadra and Nagar Haveli and Daman and Diu':
        state = 'DNDD'
    confirmedCasesIndian = data['data']['regional'][i]['confirmedCasesIndian']
    confirmedCasesForeign =  data['data']['regional'][i]['confirmedCasesForeign']
    discharged =  data['data']['regional'][i]['discharged']
    deaths =  data['data']['regional'][i]['deaths']
    total = data['data']['regional'][i]['totalConfirmed']
    print ("{:<5} {:<25} {:<25}  {:<25} {:<15} {:<15} {:<10}".format(i+1,state, confirmedCasesIndian, confirmedCasesForeign, discharged, deaths, total))
    i= i+1

# register for vaccine
def regVaccine():
   vaccine.vaccine()

#################################################################

def covidManage():

  print("\n******************************** Corona data management system *********************************\n")
  print("Enter 1 to know about Covid-19 Country Level: Cases, Deaths and Global Trends   ")
  print("Enter 2  to know about Covid-19 india Level: Cases, Deaths   ")  
  print("Enter 3 to register for vaccination : ")

  try:
   ask = int(input("\nEnter your choice : "))
   if(ask ==1):
    worldCases()
    covidManage()
   if(ask ==2):
    indiaCases()
    covidManage()
   if ask==3:
    regVaccine()
    covidManage()
   if ask>3:
      print("\nPlease enter 1, 2 or 3 only...🙏️\n")
      covidManage()
  except:
        print("\nPlease enter number only... 🙏️\n")
        covidManage()

covidManage()



