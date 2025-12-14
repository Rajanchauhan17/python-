# Create a function that returns both the area of circumference of a circle given its radius.

import math
def circle_status(radius):
    Area= math.floor(math.pi**radius)  
    circumference= math.floor(2*math.pi*radius)
    return Area,circumference
        

# print(F"Area of circumference of circle {Area_of_circumference(56) } cm")
a,b=circle_status(5)
print(f"Area of circle = {a}cm , Area of circumference of circle = {b}cm")