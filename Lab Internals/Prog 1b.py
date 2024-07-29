import datetime
name=input("Enter the name of the person ")
yob=int(input("Enter the year of birth of the person "))

current_year=datetime.date.today().year
age=current_year-yob

if(age>60):
    print("You are a senior citizen ")
else:
    print("You are not a senior citizen ")