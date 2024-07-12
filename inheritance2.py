'''
5)Create a base class Vehicle with an attribute vehicle_type. Create two derived classes Car and Bike that inherit from Vehicle. Both derived classes should have their own attributes and methods. Create objects of both Car and Bike classes and display their information.

'''

class Vehicle:
    def __int__(self,vehicle_type):
        self.vehicle_type = vehicle_type
    def display_vehicle(self):
        print(f"type of vehicle :{self.vehicle_type}")

class Car(Vehicle):
    def __int__(self,vehicle_type,model,year):
        super().__int__(vehicle_type)
        self.model = model
        self.year = year

    def display_car(self):
        super().display_vehicle()
        print(f"car model is:{self.model}, car year is:{self.year}")

class Bike(Vehicle):
    def __int__(self,vehicle_type,gear,color):
        super().__int__(vehicle_type)
        self.gear = gear
        self.color = color
    def display_bike(self):
        super().display_vehicle()
        print(f"no of gear is:{self.gear},bike color is:{self.color}")

car = Car("car","bmw",2016)
bike = Bike("bike",5,"black")
car.display_car()
bike.display_bike()







