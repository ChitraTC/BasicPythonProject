#1. create class with instance attribute

class Student:
    def __init__(self,name,regId,grade):
        self.name=name
        self.regId=regId
        self.grade=grade

s1=Student("Chitra",111,"A")
#print(f"{s1.name} ({s1.regId}) has secured {s1.grade} grade")

#2 Inheritance- Single inheritance classA->classB
class Employee():
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def test(self):
        print("I am Parent ")
class Childemployee(Employee):
    def __init__(self,name,age,sal,id):
        self.name = name
        self.age = age
        self.sal = sal
        self.id=id

pemp1=Employee("Sagar",52,1000)
print(pemp1.age)
childemp1=Childemployee("John",25,2000,153)
childemp2=Childemployee(pemp1.name,19,pemp1.sal,69)
print("c1 age :",childemp1.age)
print("Parent age",pemp1.age)
childemp2.test()






