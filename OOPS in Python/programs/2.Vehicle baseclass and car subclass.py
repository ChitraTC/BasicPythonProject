class Vehicle:
    def __init__(self,make,model,year,color,mileage):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.mileage=mileage

    def drive(self,distance):
        self.distance=distance
        print(f"The distance covered is {self.distance}km")


    def get_info(self):

        print(f"The vehicle make is{self.make} ,model is {self.model} ,year {self.year},color {self.color} and mileage is {self.mileage}")

class Car(Vehicle):
    def __init__(self,make,model,year,color,mileage,num_doors,engine_type):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.num_doors=num_doors
        self.engine_type=engine_type

    def get_info(self):
        print(f"The vehicle make is{self.make} ,model is {self.model} ,year {self.year},color {self.color} and mileage is {self.mileage} ,number of doors {self.num_doors} Engine type {self.engine_type}")

vehicle=Vehicle("AS12","BD2002",2022,"White",54.69)
vehicle.drive(100)
vehicle.get_info()

car=Car("f2","i20",2023,"Red",60.02,5,"Carbon cumbustion")
car.get_info()
