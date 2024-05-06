n=input("Numbers ")
l=[]
for i in n:
    l.append(i)
l_uni=sorted(set(l))
print(l_uni)
for i in l_uni:
    count=0
    for j in l:
        if j == i:
            count +=1
    print(f"{i} occurs {count} times ")