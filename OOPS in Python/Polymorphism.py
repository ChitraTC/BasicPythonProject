"""
Ability of an object to take different forms
Here polymorphism with inheritance
Method over riding in polymorphism:Parent and child having class with sME NAME.CHILD OVERRIDES THE PARENT AND RETURNS THE VALUE
Method overloading:A class with multiple methods with same name.Object calling same method in different ways may be with respect to the number of parameters,order of argument or datatype
"""
#polymorphism with inheritance//mothod overriding
class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price

    def show(self):
        print("Details",self.name,self.color,self.price)

    def max_speed(self):
        print("Max speed is : 150")

    def change_gear(self):
        print("Vehicle change 3 gear")

class Car(Vehicle):
    def max_speed(self):
        print("Car speed is 150")
    def change_gear(self):
        print("Change gear to 5")

car=Car('Ford',"red",250000 )
car.show()
vehicle=Vehicle("BMW","white",100000)
vehicle.show()

#polymorphism using python class:
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a Cow. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Moo")


cat1 = Cat("Kitty", 2.5)
cow1 = Cow("Fluffy", 4)

for animal in (cat1, cow1):
    animal.make_sound()
    animal.info()

