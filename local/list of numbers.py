l1=[]
odd=[]
even=[]

n=int(input("Enter the no of elements in the list "))

for num in range (n):
    num=int(input("Enter the numbers "))
    l1.append(num)
print(l1)
for j in l1:
    if j%2==0:
        even.append(j)
    else:
        odd.append(j)
print(odd)
print(even)