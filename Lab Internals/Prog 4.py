number=input("Enter the multidigit number ")
#uniq_digit={}
digit=[]
for i in number:
    digit.append(i)

uniq=sorted(set(number))
print(uniq)
for i in uniq:
    
# for i in uniq:
#     count=0
#     for j in digit:
#         if([i]==[j]):
#             count +=1
#     print(f"{i} occurs {count} times ")