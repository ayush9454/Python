import os
import string
import sys

fname=input("Enter the naame of the file ")
if not os.path.isfile(fname):
    print("File does not exist")
    sys.exit(0)

infile=open(fname,"r")
file_contents=" "

for i in infile:
    for words in i:
        if words not in string.punctuation:
            file_contents+=words
        else:
            file_contents+=" "

print(file_contents)
print("\n")

wordlist=file_contents.split()
wordfreq={}
# uniq=sorted(set(wordlist))
# for i in uniq:
#     count=0
#     for j in wordlist:
#         if[i]==[j]:
#             count+=1
#     print (f"{i} occurs {count} times")

for char in wordlist:
    wordfreq.setdefault(char,0)
    wordfreq[char]+=1
sorted_wordfreq=sorted(wordfreq.items(),key=lambda x:x[1],reverse=True)

for i in range(11):
    print(f"{sorted_wordfreq[i][0]} occurs {sorted_wordfreq[i][1]} times")