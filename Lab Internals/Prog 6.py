import os
import sys

fname=input("Enter the name of the file whose contents are to be sorted ")

if not os.path.isfile(fname):
    print("File does not exist ")
    sys.exit(0)

with open(fname,"r") as infile:
    lines=infile.readlines()

linelist=[]

for line in lines:
    linelist.append(line.strip())
linelist.sort()
print(linelist)

with open("sorted.txt","w") as outfile:
    for line in linelist:
        outfile.write(line+'\n')
print("File containing sorted.txt created successfully ")
print("Sorted.txt contains ",len(linelist),"lines")
print("Contents of sorted.txt")
rdfile=open("sorted.txt")
for line in rdfile:
    print(line,end=" ")