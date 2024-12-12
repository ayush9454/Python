class Student:
    def __init__(self,fullname):
        self.name=fullname
        print("adding a new student ")
    def welcome(self):
        print("Hello world")


s1=Student("Ayush")
print(s1.name)

s2=Student("Piyush")
print(s2.name)

s1.welcome()