class calculator:
    def addition(self):
        print(a+b)

    def subtraction(self):
        print(a-b)

    def mul(self):
        print(a * b)

    def div(self):
        print(a/b)

a=int(input("Enter the first number : "))
b=int(input("Enter the second number : "))
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")
object=calculator()
choice =int(input("Enter the choice "))
if choice==1:
    print("Sum=",object.addition())
elif choice==2:
    print("Difference= ",object.subtraction())
elif choice==3:
    print("Product=",object.mul())
elif choice==4:
    print("Quotient =",object.div())
else:print("Enter a valid Operation")


