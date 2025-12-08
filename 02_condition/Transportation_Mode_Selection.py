Distance=int(input("Enter the Distance:"))


if Distance<3:
    Mode="Walk"
elif Distance<=15 :
    Mode="Bike"
elif Distance>15:
    Mode="Car"
    
print(f"The Mode Transportation for {Distance} km is {Mode}")        