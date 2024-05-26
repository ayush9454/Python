# a=int(input("Enter a number "))

# try:
#     for i in range(1,11):
#         print(a*i)
# except ValueError:
#     print("invalid input ")

# print("Some more code ")

try:
    l=[1,5,6,7]
    i=int(input("Enter the index "))
    print(l[i])
except:
    print("Some error occured ")
finally:
    print("I am always executed ")