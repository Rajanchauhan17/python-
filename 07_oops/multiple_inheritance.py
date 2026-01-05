# Multiple inheritance 
#Create two classess Battery and Engine ,and let the ElectricCar class inherit from both ,demonstrating multiple inheritance

# 1️⃣ What is multiple inheritance?
# Multiple inheritance means a class can inherit from more than one parent class.

# class ElectricCarTwo(Battery, Engine, Car):
#     pass

# Here, ElectricCarTwo inherits from:
# Battery
# Engine
# Car
# So it gets all public methods and attributes from all three classes.



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
    
 
    
    
class Battery:
    def battery_info(self):
        return "this is battery"
    
class Engine:
    def engine_info(self):
        return "this is Engine"
    
    
class ElectricCarTwo(Battery,Engine,Car):   #🔹 What is the working of pass in Python?
     pass                                    # is a null statement in Python.
                                             #It means “do nothing”, but it is syntactically required in places where Python expects a statement  pass
                                             #pass tells Python:
                                             #“I know this block is empty for now — continue execution.”
                                                
mycar=ElectricCarTwo("hyundai","Xcent")
print(mycar.battery_info())    
print(mycar.engine_info())            