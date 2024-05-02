# n=input("Enter numbers ")
# l=[]
# for i in n:
#     l.append(i)
# print(l)
# l_uni=set(l)
# ite = 0
# for i in l:
    
#     count=0
#     if i==l[ite]:
#         count = count+1
#     ite += 1  
# print(f"{i} occurs {count} times ")
n=input("Enter numbers ")
l=[]
count =0
for i in n:
    l.append(i)
print(l)  
for i in range(len(l)):
    for j in range(len(l)):
        if(l[i]==l[j]):
            count = count+1
            print(j,count)
    count =0
    