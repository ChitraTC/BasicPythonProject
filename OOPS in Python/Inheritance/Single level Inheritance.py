class Vehicle:
    def vehicle_info(self):
        print("Inside vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside car class")

car1=Car()
car1.car_info()
car1.vehicle_info()
