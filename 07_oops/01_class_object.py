# Basic Class and Object:
#Create a Car class with attributes like brand and model.Then create an instance of this class

class Car:                                #__init__ is a constructor.
    def __init__(self,brand,model):       #It runs automatically when you create a new object from the class.
        self.brand=brand                  #self refers to the current object.
        self.model=model                  #brand and model are parameters passed while creating an object.
                                          #self.brand and self.model are instance variables that store data for each object

mycar=Car("maruti","Alto")
print(mycar.brand)        
print(mycar.model)        
    
my_car_two=Car("Tata","Safari")
print(my_car_two.model)



