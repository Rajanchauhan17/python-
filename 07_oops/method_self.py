
# Add a method to the car class that displays the full name of the car(brand,model)

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def fullname(self):
        return f"{self.brand} {self.model}"    
        
        
        
        
        
mycar=Car("maruti","Xcent")        
print(mycar.brand)
print(mycar.model)

print(mycar.fullname())