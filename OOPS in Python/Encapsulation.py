"""
It is method of protecting data using accesss modifiers(public,private,protected)
"""
#protected(single '_')
class Bank:
    def __init__(self,b_name,b_transaction):
        self.name=b_name
        self.trans=b_transaction

bank=Bank("SBI",1234589)
print(bank.name)
print(bank.trans)

#access modifiers:data to be should be prefixed with
"""
public= nothing
private="--"
protected="__"
"""

# define parent class Company
class Company:
    # constructor
    def __init__(self, name, proj):
        self.name = name  # name(name of company) is public
        self._proj = proj  # proj(current project) is protected

    # public function to show the details
    def show(self):
        print("The code of the company is = ", self._proj)


# define child class Emp
class Emp(Company):
    # constructor
    def __init__(self, eName, sal, cName, proj):
        # calling parent class constructor
        Company.__init__(self, cName, proj)
        self.name = eName  # public member variable
        self.__sal = sal  # private member variable

    # public function to show salary details
    def show_sal(self):
        print("The salary of ", self.name, " is ", self.__sal, )


# creating instance of Company class
c = Company("Stark Industries", "Mark 4")
# creating instance of Employee class
e = Emp("Steve", 9999999, c.name, c._proj)

print("Welcome to ", c.name)
print("Here ", e.name, " is working on ", e._proj)

# only the instance itself can change the __sal variable
# and to show the value we have created a public function show_sal()
e.show_sal()
e.show()
c.show()