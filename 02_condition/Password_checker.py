password=input("enter the password:")


if len(password)<6:
    print("password is weak")
elif len(password)<=10 :
    print("Password is medium")
else:
    print("password is strong")    
    