# Use a property decorator in the class to make the model attribute read-only



# When to use @property

# Use @property when you want to:

# Expose data safely

# Make attributes read-only

# Add validation later without changing the interface

# Keep clean syntax (obj.attribute instead of obj.get_attribute())

# 7️⃣ Real-world analogy

# Think of @property like:

# A glass display case 🪟

# You can see the object

# You can’t touch or change it

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.__model=model
        
    def fullname(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return f"{self.__brand} !"
    
    def fuel_type(self):
        return "Petrol or Diesal"
    
    @staticmethod
    def car_description():
        return "Car is means of transport"
    
    @property
    def model(self):
        return self.__model
    
    
class ElectricCar(Car):
    def __init__(self,brand,model,battarySize):
        super().__init__(brand,model)
        self.battarySize=battarySize
     
    def fuel_type(self):
        return "ElectricCharge"    
        
        

safari=Car("Tata","Swift")
# safari.model="city"

# print(safari.car_description())
# print(Car.car_description())
print(safari.model)


