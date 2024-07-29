import math

def mean(number):
    result=sum(number)/len(number)
    return result

def variance(number,mean):
    square_diff_sum=0
    for i in numbers:
        square_diff_sum += (i-mean)**2
    return square_diff_sum/len(numbers)

def standard_deviation(variance):
    return math.sqrt(variance)

n=int(input("Enter the number of elements you want "))
numbers=[]

for i in range(n):
    i=int(input("Enter the numbers "))
    numbers.append(i)

mean=mean(numbers)
variance=variance(numbers,mean)
s_d=standard_deviation(variance)
print(mean)
print(variance)
print(s_d)