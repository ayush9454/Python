import random

number=random.randint(1,20)
guess=6
#print(number)
while(guess>0):
    num=int(input("Enter a number "))
    if num==number:
        print("You gussed the number correctly")
        break
    elif (num<number):
        print("Too low")
    elif (num>numbwhaer):
        print("Too high")
    guess-=1
if guess==0:
    print("You ran out of chances")