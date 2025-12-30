#Modify the class to encapsulate the brand attribute ,making it private ,and provide a getter method for it

class Car:
    def __init__(self,brand,model):
        self.__brand=brand
        self.model=model
        
    def fullname(self):
        return f"{self.__brand} {self.model}"
    
    def get_brand(self):
        return f"{self.__brand} !"
    
class ElectricCar(Car):
    def __init__(self,brand,model,battarySize):
        super().__init__(brand,model)
        self.battarySize=battarySize
        
cartata=ElectricCar("Tata","Safari","45khw")
# print(cartata.__brand)  
print(cartata.get_brand())
# print(cartata.model)  
# print(cartata.battarySize)  
# print(cartata.fullname())
        
                    
        
        