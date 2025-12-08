

# Classify a person's age group based on their age input.

age=int(input("enter your age:"))
if age<13:
    print("You are a child.")
elif age>=13 and age<20:
    print("You are a teenager.")
elif age>=20 and age<65:
    
    print("You are an adult.")
else:
    print("you are a GOAT")
    