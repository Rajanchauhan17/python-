#Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar


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
    
    @staticmethod
    def car_description():
        return "Car is means of transport"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battarySize):
        super().__init__(brand,model)
        self.battarySize=battarySize
     
    def fuel_type(self):
        return "ElectricCharge"    
        
        
cartata=ElectricCar("Tata","Safari","45khw")
# print(cartata.car_description())



print(isinstance(cartata,Car))
print(isinstance(cartata,ElectricCar))

# safari=Car("Tata","Swift")
# print(safari.car_description())
# print(Car.car_description())

