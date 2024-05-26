ep1={'ayush':54,'piyush':84,'vyom':64,'ritik':75}
ep2={'vaibhav':97,'patel':74}

ep2.update(ep1)
ep2.pop('vyom') #Removes the given item from dict
ep2.popitem()  #Removes the last item from dict 
print(ep2)

# print(ep2)
# empty={}
# empty.update(ep2)
# print(empty)