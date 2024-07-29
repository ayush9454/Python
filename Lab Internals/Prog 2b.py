def factorial(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result

def binomial_coefficient(n,r):
    if n<r:
        return 0
    return factorial(n)//(factorial(n-r)*factorial(r))

n=int(input("Enter the number whose factorial you want "))
if(n<0):
    print("Factorial does not exist for negative number ")
else:
    result=factorial(n)
    print(result)

n= int(input("Enter the value of n "))
r= int(input("Enter the value of r "))
result=binomial_coefficient(n,r)
print(f"Binomial coefficient of ({n},{r}) is {result}")