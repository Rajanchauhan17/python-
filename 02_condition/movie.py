
age=int(input("Enter your age:"))
Day="Wednesday"
price=0

if age>=18:
    price=price+12
    print("price for adult $",price)
    
else:
    price=price+8
    print("price for children $",price)
    
if Day=="Wednesday":
    price=price-2
           
print('Ticket price after discount $',price)    


    
    
