import time
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
if(timestamp>'12:00:00' and timestamp<'20:59:59'):
    print("Good afternoon bro ")
elif(timestamp>'21:00:00'):
    print("Good night bro ")
else:
    print("Good morning bro ")
