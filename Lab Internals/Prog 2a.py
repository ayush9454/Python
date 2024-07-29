#n=int(input("Enter the length of sequence "))
n=7
num1=0
num2=1
print(num1,num2,sep=',',end=",")
for count in range(n-2):
    num1,num2=num2,num1+num2
    print(num2,end=",")
print('\b')