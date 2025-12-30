# Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classess,but with different behaviors.


# What Polymorphism Means Here

# Polymorphism allows the same method name (fuel_type) to behave differently depending on the object that calls it.

# Car.fuel_type() → returns fuel for normal cars

# ElectricCar.fuel_type() → overrides the parent method and returns electric power

# Even though both classes have a method called fuel_type, the object type determines which version runs.



class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        
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
print(safari.fuel_type())