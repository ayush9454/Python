f=open('C:\Programming\Python\Files\myfile.txt','r')
# text=f.write(" Hello world")
# print(text)

while True:
    line = f.readline()
    print(line)
    if not line:
        break

f.close( )