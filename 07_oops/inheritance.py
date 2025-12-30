#Create an Electric car class that inherits from Car class an additional attributes battery_size


class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def fullname(self):
        return f"{self.brand} {self.model}"    
        
        
class ElectricCar(Car):
     def __init__(self,brand,model,batterySize):
         super().__init__(brand,model)
         self.batterySize=batterySize
         
      
    
mytesla=ElectricCar("Tesla","Model Raj","80kWh")
print(mytesla.brand)          
print(mytesla.model)          
print(mytesla.batterySize)          

print(mytesla.fullname())