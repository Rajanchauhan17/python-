# score=int(input("Enter your score:"))

# if score>=90 and score<=100:
#     print("You Score a  A score ")
# elif score>=80 and score<=89:  
#     print("You Score a  B score ")
# elif score>=70 and score<=79:  
#     print("You Score a  C score ")
# elif score>=60 and score<=69:  
#     print("You Score a  D score ")
# else:
#     print("You Score a  F score ")
    
    
score=int(input("Enter your score:"))

if score>=101:
   print("Please enter valid grade")
   exit()

if score>=90:
    Grade="A"
elif score>=80:
    Grade="B"
elif score>=70:
    Grade="C"
elif score>=60:
    Grade="D"
else:
    Grade="F"
    
print("According to your score your grade is",Grade)    