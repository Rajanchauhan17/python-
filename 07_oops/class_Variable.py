# Problem : Add a class variable to Car that keeps track of the number of cars created 

 

class Car:
    totalCar=0
    
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        Car.totalCar+=1
        
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return f"{self.__brand} !"
    
    def fuel_type(self):
        return "Petrol or Diesal"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battarySize):
        super().__init__(brand,model)
        self.battarySize=battarySize
     
    def fuel_type(self):
        return "ElectricCharge"    
        
        
cartata=ElectricCar("Tata","Safari","45khw")
print(cartata.fuel_type())

safari=Car("Tata","Swift")
print(safari.totalCar)
print(Car.totalCar)