while True:
    print("Who are you?")
    name=input()
    if name != "joe":
        continue
    print("Hello joe,What is the password?")
    password=input()
    while(password!="swordfish"):
        password=str(input("Access denied, re enter password\n"))
    print("Access granted")
    print("sdsd")
    break