def DivExp(a,b):
    assert a>0,"Value of a should be greater than 0 "
    if(b==0):
        raise ValueError("Value of b should be greater than 0 ")
    return a/b

try:
    a=float(input("Enter the value of a "))
    b=float(input("Enter the value of b "))
    result=DivExp(a,b)
    print(f"Result is {result}")

except(ValueError) as ve:
    print(f"Value errot: {ve}")
except(AssertionError) as ae:
    print(f"Assertion error: {ae}")