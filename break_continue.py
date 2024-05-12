while True:
    print("Who are you?")
    name=input()
    if name != "joe":
        continue
    print("Hello joe,What is the password?")
    password=input()
    for i in range(4):

        if(password!="swordfish"):
            password=str(input("Access denied, re enter password\n"))
        else:
            print("Access granted")
            break
    #print("sdsd")
    break