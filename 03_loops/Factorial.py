Number=int(input("Enter the Number:"))
fact=1

# for i in range(1,Number+1):
#     fact=fact*i
#     i=i+1
    
# print(f"Factorial of {Number} is {fact}")    

while Number>0:
    fact=fact*Number
    Number=Number-1
print(f"Factorial  is {fact}")    