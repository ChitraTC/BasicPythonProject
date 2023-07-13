"""
A class called Employee, which models an employee with an ID, name and salary, is designed as shown in the following class diagram. The method raiseSalary(percent) increases the salary by the given percentage. Write the Employee class.

Attributes:
Id :int
Firstname:string
Lastname:string
Salary:int

Methods:


"""
class Employee:
    def __init__(self,id,firstname,lastname,salary):
        self.id=id
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
    def get_id(self):
        print(f"The employee ID is {self.id}")
    def get_firstname(self):
        print(f"The first name of employee is {self.firstname}")
    def get_lastname(self):
        print(f"The last name of employee is {self.lastname}")
    def get_Name(self):
        print(f"Full name of Employee is {self.firstname+self.lastname}")
    def get_salary(self):
        print(f"The salary of Employee is {self.salary}")
    def set_salary(self,salary):
        self.salary = salary
        #print(f"Set the salary of employee to {self.salary}Rs")
    def get_AnnualSalary(self):
        AnnualSalary=self.salary*12
        print(f"The annual salary of  {self.firstname+self.lastname} is {AnnualSalary}")
    def raise_salary(self,percentage):
        self.salary=self.salary+((percentage*self.salary)/100)
        print(f"The new salary of  {self.firstname+self.lastname} after increment is {self.salary}")
    def tostring(self):
        print(f"Employee[id={self.id} , name={self.firstname+self.lastname},salary={self.salary}]")

emp=Employee(1450,"Chitra","Degish",15000)

emp.get_id()
emp.get_firstname()
emp.get_lastname()
emp.get_Name()
emp.get_salary()
emp.get_AnnualSalary()

emp.set_salary(25000)
emp.get_AnnualSalary()

emp.raise_salary(25)
emp.get_AnnualSalary()
emp.tostring()
