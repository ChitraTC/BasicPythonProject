class Person:
    #class parameter
    name="Person"

    def __init__(self,name):
        #instance parameter
        self.name=name


obj=Person("Degish")
print(f"{Person.name} name is {obj.name}")

obj2=Person("Chitra")

print(f"{Person.name} name is {obj2.name}")
