class Myclass:
    x=6
print(Myclass)
ob=Myclass()
print(ob)
print(ob.x)
ob1=Myclass()
print(ob1)
ob1.x=7
print(ob1.x)

class Car:
    name=""
    model=2015
car1=Car()
car1.name="Ford"
car1.model=2018
print(car1.model)
print(car1.name)
print(f"{car1.name} is  {car1.model} model car")
car2=Car()
car2.name="i 20"
car2.model=2023
print(f"{car2.name} is  {car2.model} model car")

#class using constructors(__init__,__str__)
class Emp():
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def __str__(self):
        return f"{self.name}({self.id})"

    def test(self):
        print("I am perfect")
emp1=Emp("Chitra",147)
emp1.test()
print(emp1)
print(f"{emp1.name} is a permanent employee with an id of {emp1.id}")
